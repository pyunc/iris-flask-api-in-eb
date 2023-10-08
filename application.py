from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib
import sys
import os

sys.path.append('../../iris-flask-api-in-eb')
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..')))

model_filename = 'iris_model.pkl'
model = joblib.load(model_filename)

# Initialize the flask class and specify the templates directory
application = Flask(__name__, template_folder="templates")


@application.route("/")
def hello():
    return jsonify({'status': 200})

# Default route set as 'home'


@application.route('/home')
def home():
    return render_template('home.html')  # Render home.html


# Route 'classify' accepts GET request
@application.route('/classify', methods=['POST', 'GET'])
def classify_type():
    try:
        sepal_len = request.args.get('slen')  # Get parameters for sepal length
        sepal_wid = request.args.get('swid')  # Get parameters for sepal width
        petal_len = request.args.get('plen')  # Get parameters for petal length
        petal_wid = request.args.get('pwid')  # Get parameters for petal width
        # Convert to numpy array
        arr = np.array([sepal_len, sepal_wid, petal_len, petal_wid])
        arr = arr.astype(np.float64)  # Change the data type to float
        query = arr.reshape(1, -1)  # Reshape the array
        variety_mappings = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
        prediction = variety_mappings[model.predict(query)[0]]

        # Render the output in new HTML page
        return render_template('output.html', variety=prediction)
    except:
        return 'Error'


@application.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print(data)
    features = data['features']
    prediction = model.predict([features])[0]
    return jsonify({'prediction': str(prediction)})


# Run the Flask server
if (__name__ == '__main__'):
    application.run(host='0.0.0.0', port=5000, debug=True)
