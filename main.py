from flask import Flask, make_response, jsonify, request
from bd import Carros


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def get_Carros():
    return make_response(
        jsonify(
            message='Lista de carros:',
            data=Carros
        )
    )
@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify (
            mensagem= 'Carro cadastrado com sucesso!',
            carro=carro
        )
    )

app.run()
