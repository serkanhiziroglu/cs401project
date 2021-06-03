from flask import Flask, render_template, request
from flask_request_id_header.middleware import RequestID
from datetime import datetime
import pandas as pd
from data import *
import math


app = Flask(__name__)

app.config['REQUEST_ID_UNIQUE_VALUE_PREFIX'] = 'USER-' #req ID prefix
RequestID(app) # Add req ID

@app.route('/', methods=["GET"])
def index():
	return render_template('main.html')

# AI agent ile iletisim API'yi
@app.route('/getAIresponse',  methods=['POST'])
def getAIresponse():
	type = request.form.get('type').strip()
	location = request.form.get('location').strip()
	duration = request.form.get('duration').strip()
	transportation = request.form.get('transportation').strip()
	print(f'type: {type}, loation: {location}, duration: {duration}, transportation: {transportation}')
	# aiResponse = Python.run('aimodel.py', userMessage)
	aiResponse = aiModel(type, location, duration, transportation)
	return aiResponse

# Get unique user ID
@app.route('/getUserID',  methods=['GET'])
def getUserID():
	return request.environ.get("HTTP_X_REQUEST_ID")


# Test icin
@app.route('/account')
def accountPage():
	return 'This is your account page'



def aiModel(type, location, duration, transportation):

	
	

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
	# text = ""
	# if location != "TURKEY":
	# 	my_location = "TURKEY"
	# if text.lower() == "hello":
	# 	return "Hi there!"
	# elif "how are you" in text.lower():
	# 	return "I'm fine, thank you. How are you?"
	# elif "bye" in text.lower():
	# 	return "Goodbye!"
	# elif "see you" in text.lower():
	# 	return "See you later!"
	# else:
	# 	return activity, duration, "TURKEY", startTime

if __name__ == '__main__':
	app.run(debug=True)