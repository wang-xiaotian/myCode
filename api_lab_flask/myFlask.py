from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hELLO wORld'


@app.route('/hello/<name>')
def hello_name(name):
    return f'hELLO wORld {name}'

if __name__ == "__main__":
    print('listening port 3000')
    app.run(host='0.0.0.0', port = 3000)


