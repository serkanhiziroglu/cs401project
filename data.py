import pandas as pd
import random
import math

initValueArray= [0.10, 0.15, 0.20, 0.25]


#random.shuffle(initValueArray)

print(initValueArray)


locationData = {
            'AIdecision': initValueArray,
            'BudgetRequired':['High','High','High','Low'],
            'Distance':['Long', 'Short', 'Short', 'Long'],
            'Language':['English', 'Italian', 'French', 'Japanese']
            }

locations = pd.DataFrame(locationData, index= ['United States', 'Italy', 'France', 'Japan'])

countryImages= ['https://cdnuploads.aa.com.tr/uploads/Contents/2020/03/30/thumbs_b_c_a1df62a60fd46dbaba998823f183e6b5.jpg?v=013550',
'https://micedata.s3.eu-central-1.amazonaws.com/MiceProjectData/Images/2020/3/17/130_41_866fbf9c-61d6-46d8-9d8e-8a9ccae3215a.jpg',
'https://univerlist.com/media/images/blog/Greece-2560x1194.jpg',
'https://www.fodors.com/wp-content/uploads/2020/05/StatusOfAll50States__HERO_shutterstock_1548894737.jpg'
]

locations['Image'] = countryImages


typeAmericaDict = {
  "Food and Culture": "https://www.ekathimerini.com/wp-content/uploads/2021/06/statueofliberty.jpg",
  "Activity and Entertainment": "https://expatexplore.com/blog/wp-content/uploads/2018/11/New-Years-Eve-New-York-City-Travel-America-Expat-Explore.jpg",
  "Nature and Adventure": "https://www.mercurynews.com/wp-content/uploads/2019/11/SJM-Z-DelicateArchFall-1129.jpg",
  "Beach": "https://i.insider.com/5771930491058427008cbe6d?width=1000&format=jpeg&auto=webp"
}

typeFranceDict = {
  "Food and Culture": "https://www.eutouring.com/statues_in_paris_m15_DSC08734_lrg.jpg",
  "Activity and Entertainment": "https://i2.wp.com/thegoodlifefrance.com/wp-content/uploads/2018/01/nice-carnival.jpg?ssl=1",
  "Nature and Adventure": "https://www.responsiblevacation.com/imagesClient/S_152753.jpg",
  "Beach": "https://www.themediterraneantraveller.com/wp-content/uploads/2018/03/palombaggia-beach-corsica-france.jpeg"
}

typeItalyDict = {
  "Food and Culture": "https://www.commisceo-global.com/images/easyblog_articles/1817/leaning-tower-of-pisa.jpg",
  "Activity and Entertainment": "https://www.lifeinitaly.com/wp-content/uploads/2018/08/jeannette.bari_.jpg",
  "Nature and Adventure": "https://cdn1.parksmedia.wdprapps.disney.com/media/blog/wp-content/uploads/2015/01/gongon872681.jpg",
  "Beach": "https://a.cdn-hotels.com/gdcs/production193/d1872/bb6c4092-88a4-4754-9d2f-2a2ab2700ed8.jpg"
}

typeJapanDict = {
  "Food and Culture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJqYQ1ukp6kFXfQvRwecs9HymvMEs35esRDA&usqp=CAU",
  "Activity and Entertainment": "https://discovery.cathaypacific.com/wp-content/uploads/2017/06/Hero-japan-Events-Festival-1.jpg",
  "Nature and Adventure": "https://www.nationalgeographic.com/content/dam/expeditions/destinations/asia/active/japan-adventure.ngsversion.1511365177185.adapt.1900.1.jpg",
  "Beach": "https://www.planetware.com/wpimages/2020/06/japan-best-beaches-okinawa-beaches.jpg"
}


transportationAmericaDict = {
  "Train": "https://travel.home.sndimg.com/content/dam/images/travel/fullrights/2018/3/12/0/CI-Amtrak_California-Zephyr.jpg.rend.hgtvcom.616.462.suffix/1520875943365.jpeg",
  "Car": "https://blog.padi.com/wp-content/uploads/2016/08/shutterstock_358230071.jpg",
  "Cruise": "https://www.gannett-cdn.com/-mm-/f02a958f8e3aefc58c09599f576b304b0d6ee476/c=0-105-1023-683/local/-/media/2018/04/23/USATODAY/USATODAY/636601076574988475-001.jpg?width=660&height=373&fit=crop&format=pjpg&auto=webp",
  "Caravan": "https://images.squarespace-cdn.com/content/v1/5ca3e1daca525b6d60ba7012/1587238435095-DWQ0G1L0LJBQMMUNJSYK/ke17ZwdGBToddI8pDm48kHem505q6McQd8XRhQc9zkRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpxpEURhgSBEh9ILe0HKIG3CcOCklsxWwam3CdWF6Xw7jwVv5P97BEtB5XaVnmvMtTA/campervan+rentals+in+the+USA.jpeg?format=750w"
}

transportationFranceDict = {
  "Train": "https://www.tripsavvy.com/thmb/am1CzuipHlAQ2jVTnNIfB88fnuA=/2121x1193/smart/filters:no_upscale()/GettyImages-527073131-5c3396b6c9e77c0001249aee.jpg",
  "Car": "https://travelfrancebucketlist.com/wp-content/uploads/2019/09/Travel-France-by-Car-1024x683.jpg",
  "Cruise": "https://world-traveled.com/wp-content/uploads/2021/05/55922576-41742700.jpgv1619803540.jpeg",
  "Caravan": "https://st.focusedcollection.com/14026668/i/650/focused_268296548-stock-photo-france-caravan-roadside.jpg"
}

transportationItalyDict = {
  "Train": "https://www.italymagazine.com/sites/default/files/styles/800xauto/public/feature-story/leader/bigstock-italy-cinque-terre-train-at-22461182.jpg?itok=buR2GwqD",
  "Car": "https://i2.wp.com/passionpassport.com/wp-content/uploads/2017/10/italy-road-trip-davide-oricchi-480x600.jpg?resize=480%2C600",
  "Cruise": "https://avoid-crowds.com/wp-content/uploads/2019/09/civitavecchia-1400060_1920.jpg",
  "Caravan": "https://www.wandering-bird.com/wp-content/uploads/2019/10/great-dolomites-road-motorhome.jpg"
}

transportationJapanDict = {
  "Train": "https://the-shooting-star.com/wp-content/uploads/2018/05/hans-johnson-Kyushu.jpg",
  "Car": "https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/02/a0002785/img/basic/a0002785_main.jpg?20201222155816&q=80&rw=750&rh=536",
  "Cruise": "https://pbcruise.com/assets/images/japangrace/sec01_01.jpg",
  "Caravan": "https://a3.cdn.japantravel.com/photo/25363-135348/800!/travel-japan-by-campervan-135348.jpg"
}









#random.shuffle(initValueArray)

print(locations)


# x = ((countries.AIdecision[countries.AIdecision == 8].index).to_list())

# print(x[0])
# print(countries.iloc[y])




typeData = {
            'AIdecision':initValueArray
            }

types = pd.DataFrame(typeData, index= ['Food and Culture', 'Activity and Entertainment',
 'Nature and Adventure', 'Beach'])

#random.shuffle(initValueArray)

print(types)

durationData= {
            'AIdecision':initValueArray
            }

durations = pd.DataFrame(durationData, index= ['5 Days', '7 Days', '10 Days', '15 Days'])

random.shuffle(initValueArray)

print(durations)

transportationData= {
            'AIdecision':initValueArray
            }

transportations = pd.DataFrame(transportationData, index= ['Train', 'Car', 'Cruise', 'Caravan'])

print(transportations)