from flask import Blueprint, Flask, jsonify, request, redirect

contact_bp = Blueprint('contact', __name__)


@contact_bp.route('/hello/')
def hello():
    return "Hello from Contact Page"