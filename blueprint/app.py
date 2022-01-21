from flask import Flask, jsonify, request, redirect
import json
from home import home_bp
from contact import contact_bp

app = Flask(__name__)


app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(contact_bp, url_prefix='/contact')
# app.run()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)