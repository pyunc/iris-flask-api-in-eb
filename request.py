curl -X POST "http://192.168.49.2:30010/predict" -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}' 
curl -X POST "http://0.0.0.0:5000/predict" -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}' 

