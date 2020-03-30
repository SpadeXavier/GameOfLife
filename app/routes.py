from app import app  
from flask import jsonify, render_template, request 
import json 
from LifeEngine import LifeEngine
import utils

@app.route('/') 
@app.route('/index') 
def index():
	row_size = 20;
	col_size = 30;

	styles=""

	return render_template('index.html', username='Varun', col_size=range(col_size), 
		row_size=range(row_size), styles=styles) 


@app.route('/hello', methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		print('Incoming...') 
		print(type(request.get_json(force=True)))
		with open('alive_arr.txt', 'w') as outfile:
			json.dump(request.get_json(force=True), outfile)
		return 'OK', 200

	if request.method == 'GET':
		num_gens, start_arrangement = utils.getArrangementFromFile("alive_arr.txt");

		engine = LifeEngine("100x100", start_arrangement)
		full_data = engine.get_complete_simulation(num_gens=num_gens)

		print(full_data)
		return jsonify(full_data)

