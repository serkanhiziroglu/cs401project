import pandas as pd
import random
import math

array= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [1, 2, 3, 4, 5, 6, 7]

random.shuffle(array)

print(array)


countryData = {
            'AIdecision': array,
            'BudgetRequired':['High','High','Low','High','Low','High','Low','Low','High','High'],
            'Distance':['Short', 'Short', 'Short', 'Long', 'Long', 'Short', 'Long', 'Long', 'Short', 'Short'],
            'Language':['French', 'Spanish', 'Greek', 'English', 'Chinese', 'Italian', 'Spanish', 'Thai', 'German', 'English']
            }

countries = pd.DataFrame(countryData, index= ['FRANCE', 'SPAIN', 'GREECE', 'UNITED STATES', 'CHINA', 'ITALY', 'MEXICO', 'THAILAND', 'GERMANY', 'UNITED KINGDOM'])


random.shuffle(array)

print(countries)


x = ((countries.AIdecision[countries.AIdecision == 8].index).to_list())

print(x[0])
# print(countries.iloc[y])




activityData = {
            'AIdecision':array
            }

activities = pd.DataFrame(activityData, index= ['GO HIKING', 'VISIT MUSEUMS', 'GO TO CINEMA', 'JOIN WALKING TOUR', 'VISIT CAVES', 
'GO CAMPING', 'GO SKIING', 'EAT TRADITIONAL FOOD', 'GO TO THEATRE', 'GO SWIMMING'])

random.shuffle(array2)

print(activities)

durationData= {
            'AIdecision':array2
            }

durations = pd.DataFrame(durationData, index= ['2 WEEKS', '3 WEEKS', '1 MONTH', '1 WEEKS', '3 DAYS', 
'4 DAYS', '2 MONTH'])

random.shuffle(array2)

print(durations)

startingTimeData= {
            'AIdecision':array2
            }

startingTimes = pd.DataFrame(startingTimeData, index= ['NEXT WEEK', '3 DAYS', 'TODAY', '10 DAYS', '2 WEEKS', 'NEXT MONTH', 'NEXT YEAR'])

print(startingTimes)