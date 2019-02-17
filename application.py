'''
Created on Feb 16, 2019

@author: vinas
'''

'''from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def ajaxTest():
    return 'Hello there!'

@app.route('/post', methods = ['POST'])
def talk():
    data = request.json['mg']
    msg = 'done';
    return jsonify({"msg": msg})

if __name__ == '__main__':
    app.run(debug = True)'''