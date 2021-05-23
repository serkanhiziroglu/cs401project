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

countryImages= ['https://cdnuploads.aa.com.tr/uploads/Contents/2020/03/30/thumbs_b_c_a1df62a60fd46dbaba998823f183e6b5.jpg?v=013550',
'https://micedata.s3.eu-central-1.amazonaws.com/MiceProjectData/Images/2020/3/17/130_41_866fbf9c-61d6-46d8-9d8e-8a9ccae3215a.jpg',
'https://univerlist.com/media/images/blog/Greece-2560x1194.jpg',
'https://www.fodors.com/wp-content/uploads/2020/05/StatusOfAll50States__HERO_shutterstock_1548894737.jpg',
'http://img.emg-services.net/htmlpages/htmlpage3970/china-main-1.jpg',
'https://initalycom.files.wordpress.com/2019/12/italy-city-rome.jpg?w=1200',
'https://cdn.turkishairlines.com/m/7b0235492e35e9ac/original/1400-660-jpg.jpg',
'https://www.volunteeringsolutions.com/asset/uploads/img/page_header_image/thailand/bangkok/679/679_thailand.jpg',
'https://assets.kpmg/is/image/kpmg/berlin-skyline-with-spree-river-at-sunset-germany:cq5dam.web.1200.630',
'https://s30876.pcdn.co/wp-content/uploads/london-1170x630.jpg'
]

countries['Image'] = countryImages


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

durations = pd.DataFrame(durationData, index= ['2 WEEKS', '3 WEEKS', '1 MONTH', '1 WEEK', '3 DAYS', 
'4 DAYS', '2 MONTHS'])

random.shuffle(array2)

print(durations)

startingTimeData= {
            'AIdecision':array2
            }

startingTimes = pd.DataFrame(startingTimeData, index= ['NEXT WEEK', '3 DAYS', 'TODAY', '10 DAYS', '2 WEEKS', 'NEXT MONTH', 'NEXT YEAR'])

print(startingTimes)