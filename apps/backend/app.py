from flask import Flask
from config import PORT

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)