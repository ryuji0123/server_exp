from time import sleep
from argparse import ArgumentParser
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello from flask\n"
    return name

@app.route('/cache')
def good():
    response_str = "Is this cached?\n"
    return response_str

@app.route('/domain')
def domain():
    response_str = "Hello from ns.main.com\n"
    return response_str

@app.route('/limited_connect')
def limited_connect():
    sleep(1)
    name = "Hello from connection limited flask\n"
    return name



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--port", default=80)
    args = parser.parse_args()
    app.run(debug=True, host='0.0.0.0', port=args.port)