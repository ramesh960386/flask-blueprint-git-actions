from flask import Blueprint, Flask, jsonify, request, redirect

home_bp = Blueprint('home', __name__)


@home_bp.route('/hello/')
def hello():
    return "Hello from Home Page"


@home_bp.route('/test/', methods=['GET', 'POST'])
def test():
    args = request.args.get('pid')
    json_data = request.json
    return jsonify({
        'args' : args,
        'json_data': json_data
        })