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
	activity = request.form.get('activity').strip()
	duration = request.form.get('duration').strip()
	location = request.form.get('location').strip()
	startTime = request.form.get('startTime').strip()
	print(f'activity: {activity}, duration: {duration}, location: {location}, startTime: {startTime}')
	# aiResponse = Python.run('aimodel.py', userMessage)
	aiResponse = aiModel(activity, duration, location, startTime)
	return aiResponse

# Get unique user ID
@app.route('/getUserID',  methods=['GET'])
def getUserID():
	return request.environ.get("HTTP_X_REQUEST_ID")


# Test icin
@app.route('/account')
def accountPage():
	return 'This is your account page'


def aiModel(activity, duration, location, startTime):

	x= countries.loc[location]['AIdecision']
	y = math.floor((x + 10)/2)
	z = ((countries.AIdecision[countries.AIdecision == y].index).to_list())
	location = z[0]

	x= activities.loc[activity]['AIdecision']
	y = math.floor((x + 10)/2)
	z = ((activities.AIdecision[activities.AIdecision == y].index).to_list())
	activity = z[0]

	x= durations.loc[duration]['AIdecision']
	y = math.floor((x + 7)/2)
	z = ((durations.AIdecision[durations.AIdecision == y].index).to_list())
	duration = z[0]

	x= startingTimes.loc[startTime]['AIdecision']
	y = math.floor((x + 7)/2)
	z = ((startingTimes.AIdecision[startingTimes.AIdecision == y].index).to_list())
	startTime = z[0]
	
	imageSource = countries.loc[location]['Image']
	#console.log(imageSource)

	return {
			"activity": activity,
			"duration": duration,
			"location": location,
			"startTime": startTime,
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