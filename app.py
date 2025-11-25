from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Examen CI/CD - Version 1.0.5 - Funcionando correctamente"

# Simulación de una IA simple
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'value' not in data:
        return jsonify({'error': 'No value provided'}), 400
    
    value = float(data['value'])
    # Regla: > 50 es Alto Impacto, <= 50 es Bajo Impacto
    prediction = "Alto Impacto" if value > 50 else "Bajo Impacto"
    
    return jsonify({
        'input': value,
        'prediction': prediction,
        'model_version': '1.0.5'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)