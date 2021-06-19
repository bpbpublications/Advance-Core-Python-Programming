from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return 'Hello World!'

@app.route('/welcome/<name>')
def welcomeUser(e):
    return '<h1> {} We Welcome you to our Page!!'.format(name)

if __name__ == '__main__':
    app.run(port=5000,debug=True)

