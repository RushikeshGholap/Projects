from sklearn.externals import joblib
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<inp>')
def predict_category(inp):
    responsibility = [str(inp)]
    model = joblib.load('test_model.pkl')
    output = model.predict(responsibility)[0]
    return jsonify(category = output)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)