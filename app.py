from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Seva, great job in building your first CI/CD Pipeline, keep it up.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
