from flask import Flask, jsonify, make_response

app = Flask(__name__)

desenvolvedores = [
    {"id": "0",
        "nome": "Gil Xavier",
     "habilidades": ["Python", "Flask"]},

    {"id": "1",
        "nome": "Iury Assuncao",
     "habilidades": ["JavaScript", "TypeScript"]},
    
    {"id": "2",
        "nome": "Alexandre Faria da Silva",
        "habilidades": ["Desenvolvedor de APIs e Microsservicos", "Professor Universitario"]}
]

@app.route("/")
def helloWorld():
    return ("Hello World")

# Buscar um desenvolvedor pelo ID
@app.route("/dev/<int:id>/", methods=["GET"])
def get_developer(id):
    try:
        response = desenvolvedores[id]
        status_code = 200
    except IndexError:
        mensagem = f"Desenvolvedor de ID {id} nao existe"
        status_code = 404
        response = {"status": "erro", "mensagem": mensagem, "Codigo de erro": status_code}
    except Exception as e:
        mensagem = f"Erro desconhecido: {str(e)}"
        response = {"status": "erro", "mensagem": mensagem}
        status_code = 500
    
    return make_response(jsonify(response), status_code)

#Listar todos os desenvolvedores
@app.route("/dev/", methods=["GET"])
def list_developers():
    response = desenvolvedores
    status_code = 200
    return make_response(jsonify(response), status_code)

if __name__ == "__main__":
    app.run(debug=True)
