from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Plantilla HTML sencilla integrada en el código para no complicarnos con carpetas
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Examen IA - Banda</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; width: 400px; }
        h1 { color: #333; }
        .badge { background: #28a745; color: white; padding: 5px 10px; border-radius: 20px; font-size: 0.8em; }
        input { padding: 12px; border-radius: 5px; border: 1px solid #ddd; width: 70%; margin-top: 20px; }
        button { padding: 12px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; margin-top: 10px; }
        button:hover { background-color: #0056b3; }
        .result { margin-top: 20px; padding: 15px; background-color: #e9ecef; border-radius: 5px; font-weight: bold; color: #495057; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Modelo Predictivo IA</h1>
        <p>Examen CI/CD - Version <span class="badge">1.0.5</span></p>
        <p>Funcionando correctamente en VPS</p>
        
        <form method="post" action="/predict-ui">
            <input type="number" name="value" placeholder="Ingresa un valor (ej: 80)" required>
            <br>
            <button type="submit">Analizar Impacto</button>
        </form>

        {% if prediction %}
        <div class="result">
            Resultado: {{ prediction }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# Endpoint para la interfaz web (Formulario)
@app.route('/predict-ui', methods=['POST'])
def predict_ui():
    try:
        value = float(request.form.get('value', 0))
        # Lógica simulada de IA
        prediction = "🔥 ALTO IMPACTO" if value > 50 else "🍃 BAJO IMPACTO"
        return render_template_string(HTML_TEMPLATE, prediction=prediction)
    except:
        return render_template_string(HTML_TEMPLATE, prediction="Error en el valor")

# Endpoint API JSON (Para mantener contentos a los tests automatizados)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'value' not in data:
        return jsonify({'error': 'No value provided'}), 400
    
    value = float(data['value'])
    prediction = "Alto Impacto" if value > 50 else "Bajo Impacto"
    
    return jsonify({
        'input': value,
        'prediction': prediction,
        'model_version': '1.0.5'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)