#from urllib import response
from flask import Flask, render_template

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')


@app.before_request
def before_request():
    print('Esperando la peticion...')



@app.route("/")
def home():
    return render_template('index.html')


    
if __name__ == '__main__':
    
    app.run(debug = True, port=5000)