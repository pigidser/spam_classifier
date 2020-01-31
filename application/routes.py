# classifier/application/routes.py
from flask import Flask
from flask import request, jsonify
from application import app
from spam_classifier import classify

'''Cкрипт run.py находится на верхнем уровне и содержит всего одну строку, которая
импортирует экземпляр приложения: from application import app
'''

@app.route('/classify_text', methods=['POST'])

def classify_text():
    data = request.json
    text = data['text']
    result = classify(text)
    return jsonify({'result': result})

@app.route('/number_inc', methods=['GET'])

def number_inc():
	args = request.args
	try:
		num = int(args['num']) + 1
		return str(num)
	except:
		return 'Необходимо ввести число'

@app.route('/')

def hello_world():
    return 'Hello, World!' #возвращает приветствие в виде строки.
	
@app.route('/hello_user', methods=['POST'])

def hello_user():
    data = request.json
    user = data['user']
    return f'hello {user}'
	
