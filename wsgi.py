'''
Created on Feb 16, 2019

@author: vinas
'''

from flask import Flask, render_template, request, jsonify

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/test')
def ajaxTest():
    return 'Hello there!'

@application.route('/post', methods = ['POST'])
def talk():
    data = request.json['mg']
    msg = 'done';
    return jsonify({"msg": msg})

if __name__ == '__main__':
    application.run(debug = True)