from flask import Flask

#__name__ = '__main__'  # Esse é o nome do módulo principal da aplicação. Ele é utilizado para identificar se o módulo está sendo executado diretamente ou importado como um módulo.
app = Flask(__name__)

@app.route('/')  # Esse é o decorator que define a rota da aplicação. Ele é utilizado para mapear uma URL para uma função.
def hello_world():  # Essa é a função que será executada quando a rota for acessada. Ela retorna uma string que será exibida no navegador.
    return 'Hello, World!'  # Essa é a string que será exibida no navegador quando a rota for acessada.

@app.route('/about')  # Esse é o decorator que define a rota da aplicação. Ele é utilizado para mapear uma URL para uma função.
def about():  # Essa é a função que será executada quando a rota for acessada. Ela retorna uma string que será exibida no navegador.
    return 'This is a simple Flask application.'  # Essa é a string que será exibida no navegador quando a rota for acessada.

if __name__ == '__main__':  # Esse é o ponto de entrada da aplicação. Ele é utilizado para verificar se o módulo está sendo executado diretamente ou importado como um módulo.
    app.run(debug=True)  # Esse é o método que inicia a aplicação. Ele é utilizado para iniciar o servidor web e permitir que a aplicação seja acessada pelo navegador. O parâmetro debug=True é utilizado para habilitar o modo de depuração, que permite que a aplicação seja reiniciada automaticamente quando houver alterações no código.