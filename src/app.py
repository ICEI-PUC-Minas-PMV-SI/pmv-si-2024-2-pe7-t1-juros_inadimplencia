from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from modelo import calcular
from flask import Flask, request, jsonify

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir requisições do front-end

@app.route('/simular', methods=['POST'])
def simular():
    data = request.json
    prazo = data.get('prazo')
    ipca = float(data.get('ipca', 0))
    selic = float(data.get('selic', 0))
    conf = float(data.get('conf', 0))

    # Lógica de simulação (substitua com o cálculo real)
    resultado = ipca + selic + conf + int(prazo)  # Apenas um exemplo

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
