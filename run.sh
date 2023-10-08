python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python application.py
rm -rf .venv
zip -vr application.zip ./