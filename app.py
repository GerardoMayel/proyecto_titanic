from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Carga el modelo entrenado
model = joblib.load('models/model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([list(data.values())])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)