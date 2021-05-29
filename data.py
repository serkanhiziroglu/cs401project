import pandas as pd
import random
import math

array= [1, 2, 3, 4]


random.shuffle(array)

print(array)


locationData = {
            'AIdecision': array,
            'BudgetRequired':['High','High','Low','High'],
            'Distance':['Short', 'Short', 'Short', 'Long'],
            'Language':['French', 'Spanish', 'Greek', 'English']
            }

locations = pd.DataFrame(locationData, index= ['United States', 'Italy', 'France', 'Japan'])

countryImages= ['https://cdnuploads.aa.com.tr/uploads/Contents/2020/03/30/thumbs_b_c_a1df62a60fd46dbaba998823f183e6b5.jpg?v=013550',
'https://micedata.s3.eu-central-1.amazonaws.com/MiceProjectData/Images/2020/3/17/130_41_866fbf9c-61d6-46d8-9d8e-8a9ccae3215a.jpg',
'https://univerlist.com/media/images/blog/Greece-2560x1194.jpg',
'https://www.fodors.com/wp-content/uploads/2020/05/StatusOfAll50States__HERO_shutterstock_1548894737.jpg'
]

locations['Image'] = countryImages


random.shuffle(array)

print(locations)


# x = ((countries.AIdecision[countries.AIdecision == 8].index).to_list())

# print(x[0])
# print(countries.iloc[y])




typeData = {
            'AIdecision':array
            }

types = pd.DataFrame(typeData, index= ['Food and Culture', 'Activity and Entartainment',
 'Nature and Adventure', 'Beach'])

random.shuffle(array)

print(types)

durationData= {
            'AIdecision':array
            }

durations = pd.DataFrame(durationData, index= ['5 Days', '7 Days', '10 Days', '15 Days'])

random.shuffle(array)

print(durations)

transportationData= {
            'AIdecision':array
            }

transportations = pd.DataFrame(transportationData, index= ['Train', 'Car', 'Cruise', 'Caravan'])

print(transportations)