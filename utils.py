import json 

def getArrangementFromFile(file_name):
	message = []
	with open(file_name, 'r') as infile:
		message = json.load(infile)

	# -- remember first element is number of generations user has set 
	num_gens = int(message[0])
	message = message[1:]
	print(num_gens)

	# parse ids 
	formatted_message = []
	for x in message:
		row, col = x[1:].split('-')
		row = int(row)
		col = int(col)
		formatted_message.append(tuple([row, col]))

	print(formatted_message)
	# conver to dictionary with pos: status as key,value pairs 
	start_arrangement = {}
	for pos in formatted_message:
		start_arrangement[pos] = "Alive"

	print(start_arrangement)
	return num_gens, start_arrangement