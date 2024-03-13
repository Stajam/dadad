from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'

#rota para a questao 1
@app.route('/noticia')
def noticia():
  return render_template('noticia.html')

#rota para a questão 2
@app.route('/login')
def login():
  return render_template('login.html')

#rota para a questão 3
@app.route('/arearestrita/<estado>')
def arearestrita(estado):
  return render_template('arearestrita.html', estado=estado)

#rota para a questão 4
@app.route('/tema/<tema>')
def tema(tema):
  return render_template('tema.html', tema=tema)

#rota para a questão 5
@app.route('/galeria/<imagem>')
def galeria(imagem):
  return render_template('galeria.html', imagem=imagem)

if __name__== '__main__':
  app.run()
