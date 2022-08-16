from flask import Flask
app = Flask(__name__)

@app.route
def hello_world():
    return 'Hello, boge! 21.04.11.01'

@app.route('/gg/<username>')
def hello(username):
    return 'welcome' + ': ' + username + '!'