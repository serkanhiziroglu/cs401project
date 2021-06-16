from flask import Flask, render_template, request
from flask_request_id_header.middleware import RequestID
from datetime import datetime, time
import pandas as pd
from data import *
import math
import random


app = Flask(__name__)

app.config['REQUEST_ID_UNIQUE_VALUE_PREFIX'] = 'USER-' #req ID prefix
RequestID(app) # Add req ID

user_selection_history = dict()
agent_selection_history = dict()
MAX_TIME = 60

imageSource = "";
imageSource2 = " ";


P0 = 0.94
P1 = 0.5
P2 = 0.4
P3 = 0.8 # mimic

W = 1

N = 4 # WINDOW - last n consecutive bids



@app.route('/', methods=["GET"])
def index():
	return render_template('main.html')


@app.route('/getAIresponse',  methods=['POST'])
def getAIresponse():
	type = request.form.get('type')
	user_id = request.form.get('user_id')
	print("REQUEST - User ID is : " + user_id)
	
	init_user_history(user_id)
	init_agent_history(user_id)

	
	time_remaining = request.form.get('timeleft')
	print("Remainign time for user is : " + time_remaining)
	location = request.form.get('location').strip()
	duration = request.form.get('duration').strip()
	transportation = request.form.get('transportation').strip()
	print(f'type: {type}, loation: {location}, duration: {duration}, transportation: {transportation}')

	add_selection_to_user_history(user_id, type, location, duration, transportation)

	# target_utility = calculate_TU_hybrid(user_id, time_remaining)

	aiResponse = aiModel(user_id, time_remaining)


	return aiResponse

# Get unique user ID
@app.route('/getUserID',  methods=['GET'])
def getUserID():
	return request.environ.get("HTTP_X_REQUEST_ID")

def calculate_TU_hybrid(type, location, duration, transportation, timeleft, user_id):
	t = float(timeleft) / MAX_TIME
	TUtimes = calculate_TU_times(timeleft)
	TUbehavior = calculate_TU_behavior(type, location, duration, transportation, timeleft, user_id)
	#print(t, TUtimes, TUbehavior)
	return (t**2 * TUtimes) + ( (1-t**2) * TUbehavior ) 

def calculate_TU_times(timeleft): # Formula 2
	t = float(timeleft) / MAX_TIME # scaled t
	return ( (1-t**2) * P0 ) + ( 2 * (1-t) * t * P1 ) + ( t**2 * P2)

def calculate_TU_behavior(type, location, duration, transportation, timeleft, user_id):


	utility = calculate_utility(type, location, duration, transportation)
	#print(type(past_offers[-1][4]))
	


	# past_offers = user_selection_history[user_id]
	# if len(past_offers) < 1:
	# 	return

	# past_offers = user_selection_history[user_id]
	# if len(past_offers) < 1:
	# 	return

	# most_recent_offer_utility = past_offers[-1][4] # index 4 is utility

	gamma = calculate_gamma(timeleft)
	delta_U = calculate_delta_U(user_id)

	return (utility - (gamma * delta_U))



def calculate_gamma(timeleft):
	return P3 + ((float(timeleft)/MAX_TIME) * P3)

def calculate_delta_U(user_id):
	past_offers = user_selection_history[user_id]
	delta_U = 0
	delta_U_range = min(N, len(past_offers))

	for index in range(1, delta_U_range):
		value = W * (past_offers[len(past_offers)-index][4] - past_offers[len(past_offers)-index-1][4]) # index 4 is utility
		delta_U += value

	return delta_U

def calculate_utility(type, location, duration, transportation):
	typeU = types.loc[type]['AIdecision']
	locationU = locations.loc[location]['AIdecision']
	durationU = durations.loc[duration]['AIdecision']
	transportationU = transportations.loc[transportation]['AIdecision']
	return typeU + locationU + durationU + transportationU

def add_selection_to_agent_history(user_id, type, location, duration, transportation):
	utility = calculate_utility(type, location, duration, transportation)
	agent_selection_history[user_id].append(
		(type, location, duration, transportation, utility)
	)



def add_selection_to_user_history(user_id, type, location, duration, transportation):
	utility = calculate_utility(type, location, duration, transportation)
	user_selection_history[user_id].append(
		(type, location, duration, transportation, utility)
	)

def init_user_history(user_id):
	if user_id in user_selection_history:
		return
	else:
		user_selection_history[user_id] = []


def init_agent_history(user_id):
	if user_id in agent_selection_history:
		return
	else:
		agent_selection_history[user_id] = []


# Test icin
@app.route('/account')
def accountPage():
	return 'This is your account page'

def return_current_bestoffer(user_id):
	max_utility = 0
	selection = None
	for t in types.index:
		for l in locations.index:
			for d in durations.index:
				for transport in transportations.index:
					utility = calculate_utility(t,l,d,transport)
					if utility > max_utility:
						max_utility = utility
						selection = (t, l, d, transport)
	add_selection_to_agent_history(user_id, selection[0], selection[1], selection[2], selection[3])
	
	if selection[1] == "France":
		imageSource = typeFranceDict[selection[0]]
		imageSource2 = transportationFranceDict[selection[3]]
	if selection[1] == "United States":
		imageSource = typeAmericaDict[selection[0]]
		imageSource2 = transportationAmericaDict[selection[3]]
	if selection[1] == "Italy":
		imageSource = typeItalyDict[selection[0]]
		imageSource2 = transportationItalyDict[selection[3]]
	if selection[1] == "Japan":
		imageSource = typeJapanDict[selection[0]]
		imageSource2 = transportationJapanDict[selection[3]]

	return {
				"type": selection[0],
				"location": selection[1],
				"duration": selection[2],
				"transportation": selection[3],
				"timestamp": datetime.now(),
				"imageSource": imageSource,
				"imageSource2": imageSource2
			}



def aiModel(user_id, time_remaining):


	max_utility = 0
	selection = None
	if len(agent_selection_history[user_id]) == 0:
		return return_current_bestoffer(user_id)

	t,l,d,transport,u = agent_selection_history[user_id][-1]
	target_utility = calculate_TU_hybrid(t, l, d, transport, time_remaining, user_id)
	offer_counter = 0
	offer_counter_limit = 4*4*4*4
	while offer_counter < offer_counter_limit:
		offer_counter += 1
		t_index = random.randint(0,3)
		l_index = random.randint(0,3)
		d_index = random.randint(0,3)
		transport_index = random.randint(0,3)
		#print (t_index, l_index, d_index, transport_index)
		utility = calculate_utility(types.index[t_index], locations.index[l_index], 
		durations.index[d_index], transportations.index[transport_index])
		print("TARGET UTILITY: " + str(target_utility))
		print("UTILITY: " + str(utility))
		if utility >= target_utility:
			add_selection_to_agent_history(user_id, types.index[t_index], locations.index[l_index], 
			durations.index[d_index], transportations.index[transport_index])
			selection = (types.index[t_index], locations.index[l_index], 
			durations.index[d_index], transportations.index[transport_index])
			if selection[1] == "France":
				imageSource = typeFranceDict[selection[0]]
				imageSource2 = transportationFranceDict[selection[3]]
			if selection[1] == "United States":
				imageSource = typeAmericaDict[selection[0]]
				imageSource2 = transportationAmericaDict[selection[3]]
			if selection[1] == "Italy":
				imageSource = typeItalyDict[selection[0]]
				imageSource2 = transportationItalyDict[selection[3]]
			if selection[1] == "Japan":
				imageSource = typeJapanDict[selection[0]]
				imageSource2 = transportationJapanDict[selection[3]]

			return {
				"type": selection[0],
				"location": selection[1],
				"duration": selection[2],
				"transportation": selection[3],
				"timestamp": datetime.now(),
				"imageSource": imageSource,
				"imageSource2": imageSource2
			}

	return return_current_bestoffer(user_id)




	




'''
x= types.loc[type]['AIdecision']
y = math.floor((x + 4)/2)
z = ((types.AIdecision[types.AIdecision == y].index).to_list())
type = z[0]

x= locations.loc[location]['AIdecision']
y = math.floor((x + 4)/2)
z = ((locations.AIdecision[locations.AIdecision == y].index).to_list())
location = z[0]

x= durations.loc[duration]['AIdecision']
y = math.floor((x + 4)/2)
z = ((durations.AIdecision[durations.AIdecision == y].index).to_list())
duration = z[0]

x= transportations.loc[transportation]['AIdecision']
y = math.floor((x + 4)/2)
z = ((transportations.AIdecision[transportations.AIdecision == y].index).to_list())
transportation = z[0]

imageSource = locations.loc[location]['Image']

return {
		"type": type,
		"location": location,
		"duration": duration,
		"transportation": transportation,
		"timestamp": datetime.now(),
		"imageSource": imageSource
	}
'''

if __name__ == '__main__':
	app.run(debug=True)