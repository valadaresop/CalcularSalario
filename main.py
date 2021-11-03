from flask import Flask,jsonify

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)


@app.route('/')
def home():
    return '<h2>Página Principal</h2>'

@app.route('/cadastro')
def cadastro():
    return "<h2>Pagina de Cadastro dos Empregados</h2>"

@app.route('/json')
def jason():
    return jsonify({'text':'Texto em formato Json!'})
