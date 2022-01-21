from flask import Flask, jsonify, request, redirect
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!'


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/api/<int:num>/', methods=['GET', 'POST'])
def incrementer(num):
    return "Incremented number is " + str(num+1)


@app.route('/api/<string:name>/', methods=['GET', 'POST'])
def hello(name):
    return "Hello " + name


@app.route('/api/persone/', methods=['GET'])
def persons():
    return jsonify({
        'name':'ramesh',
        'address': 'kukatpally'
        })

@app.route('/api/listdata/')
def list_data():
    return jsonify(list(range(5)))



@app.before_request
def before():
    print("This is executed BEFORE each request.")
    

@app.route('/before_request/')
def before_request():
    return "Hello World!"


###POST Data#####
@app.route('/request_data/', methods=['POST'])
def reqData():
    data = json.loads(request.data)
    print('raw data: ',data)
    # return data['deviceId']
    return data


@app.route('/request_json/', methods=['POST'])
def reqJson():
    data = request.json # or request.get_json()
    print('json data: ',data)
    return data['deviceId']

@app.route('/request_args/', methods=['POST'])
def reqArgs():
    accountId = request.args.get('accountId') #or request.args['accountId']
    # http://localhost:105/request_args?accountId=100
    # return accountId
    print('auth: ', request.authorization)
    return redirect('/home/')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)