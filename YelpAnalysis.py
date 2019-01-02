import pandas as pd
import numpy as np
import os.path
import glob
import matplotlib.pyplot as plt
import io
import csv
import random
from datetime import date, time, datetime as dt
from sklearn import linear_model 
from sklearn.metrics import mean_absolute_error
import plotly
import scipy.stats as scs
from matplotlib import style
import pandas_datareader.data as web
import seaborn as sn
from pprint import pprint as print
import json
from pathlib import Path
from time import clock
from typing import Dict, List
from pandas.io.json import json_normalize
from flatten_json import flatten
import ast
import re



# with open('/Users/ericrivetna/desktop/Data Analysis/restaurant analysis/yelp_dataset/yelp_test.json') as f:
#     data = [json.loads(line) for line in f]
#     df = pd.DataFrame(data)

# df = df.to_csv('./Hello.csv')
# df = pd.read_csv('./Hello.csv')



"""
Creates a list of files for input/output using os library
"""
# files = os.listdir(os.getcwd())
# json_list = []
# csv_list = []
# for files in glob.glob('*.json'):
#     json_files = os.path.abspath(files)
#     json_list.append(json_files)
#     csv_files = json_files.replace('.json','.csv')
#     csv_list.append(csv_files)

# def json_to_csv(json_in, csv_out):
"""
Quickly putting .json into .csv using the Pandas Library. 
This is quick and janky. There are better ways to learn to do this.  
"""
#     with open (json_in) as f:
#          data = [json.loads(line) for line in f]
#          data = data.to_csv(csv_out)
#     return data

# for i, c in (json_list, csv_list):
#     json_to_csv(json_in, csv_out)



foo = {"address": "746 Street Clair Avenue W",
    "attributes": {"BikeParking": "True",
                   "BusinessAcceptsCreditCards": "True",
                   "BusinessParking": "{'garage': False}, 'street': False,'validated': False, 'lot': False, 'valet': False}",     
                   "OutdoorSeating": "False",
                   "RestaurantsDelivery": "False",
                   "RestaurantsPriceRange2": "2",
                   "RestaurantsTakeOut": "True",
                   "WiFi": "no"},
    "business_id": "5J3b7j3Fzo9ISjChmoUoUA",
    "categories": "Food, Bakeries, Coffee & Tea",
    "city": "Toronto",
    "hours": {"Friday": "7:30-19:0",
              "Monday": "7:30-19:0",
              "Saturday": "8:0-18:0",
              "Sunday": "9:0-18:0",
              "Thursday": "7:30-19:0",
              "Tuesday": "7:30-19:0",
              "Wednesday": "7:30-19:0"},
    "is_open": 1,
    "latitude": 43.6813277,
    "longitude": -79.4278838,
    "name": "Mabel's Bakery",
    "neighborhood": "Wychwood",
    "postal_code": "M6C 1B5",
    "review_count": 23,
    "stars": 4.0,
    "state": "ON"}


with open('./yelp_test.json', 'r') as f:
    data = [json.loads(line) for line in f]



yelp_biz_data = json_normalize(data)
yelpBizDf = pd.DataFrame(yelp_biz_data)
"""
This is my incredibly novice way of cleaning the file. 
Manual work was performed on the CSV for certain items
"""
yelpBizDf.rename(columns = lambda x: x.replace('attributes.','')[0:],inplace = True)
yelpBizDf.rename(columns = lambda x: x.replace('hours.','')[0:],inplace = True)
yelpBizDf.rename(columns = lambda x: re.sub(r'\B([A-Z])', r' \1', x), inplace = True)
newWeeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
oldWeeks = yelpBizDf.columns[41:48]
yelpBizDf.rename(columns=dict(zip(oldWeeks,newWeeks)), inplace = True)


# for i in newWeeks:
#     print(yelpBizDf[i].values)


foo1 ='10:0-23:0'
# foo3 = 'asfkjaslkf'
# if foo1[4] == '-':
#     print(foo1[:4] + '0' + foo1[4:])
# else:
#     print('nah')



def fix_time():
    for i in newWeeks:
        pattern_1 = re.compile(r'(\d{2}\D\d)(\D)(\d{2}\D\d)')
        pattern_2 = re.compile(r'(\d\D\d)(\D)(\d{2}\D\d)')
        pattern_4 = re.compile(r'(\d\d\D\d)(\D)(\d+\D\d)')
        pattern_3 = re.compile(r'(\d\D\d+)(\D)(\d\d\D\d)')
        pattern_5 = re.compile(r'(\d\D\d+)(\D)(\d\d\D\d\d)(\d)')
        pattern_6 = re.compile(r'(\d+\D\d+)(\D)(\d\D\d)')
        twenty_four_hour = re.compile(r'(\d\D\d)(\D)(\d\D\d)')
        repl = r'\g<1>0\2\3'
        repl_2 = r'\1\2\g<3>0'
        repl_3 = r'\1\2\3'

        yelpBizDf[i] = pd.Series(yelpBizDf[i]).str.replace(pattern_1, repl, regex = True)
        yelpBizDf[i] = pd.Series(yelpBizDf[i]).str.replace(pattern_2, repl, regex = True)
        yelpBizDf[i] = pd.Series(yelpBizDf[i]).str.replace(pattern_3, repl_2, regex = True)
        yelpBizDf[i] = pd.Series(yelpBizDf[i]).str.replace(pattern_4, repl, regex = True)
        yelpBizDf[i] = pd.Series(yelpBizDf[i]).str.replace(pattern_5, repl_3, regex = True)
        yelpBizDf[i] = pd.Series(yelpBizDf[i]).str.replace(twenty_four_hour, '24 Hours', regex = True)
        yelpBizDf[i] = pd.Series(yelpBizDf[i]).str.replace(pattern_6, repl_2, regex = True)
        write_csv = yelpBizDf.to_csv('./yelp_academic_dataset_business_func2.csv')
        open_csv = pd.read_csv('./yelp_academic_dataset_business_func2.csv')
        df = pd.DataFrame(open_csv)
        return df


# fix_time()

yelpDf = fix_time()

print(yelpDf.shape)


    







# # for i in newWeeks:
#     print(type(pd.Series(yelpBizDf[i].to_string)))


# print(re.sub(r'\d\d|:|\d|-|\d\d|:|\d','\10\2',foo1))
# for i in newWeeks:
#     print(yelpBizDf['Monday'].rename(columns = lambda x: re.sub((r'(\d|:|\d)(|-|\d\d|:|\d)'),r'',x)))








   







#json_normalize(foo_1["attributes.Ambience"],foo_1['attributes.BusinessParking'],foo_1["attributes.GoodForMeal"])
# bar = pd.DataFrame(foo_1)
# bar = bar.set_index(keys="name")
# zab = bar["attributes.Ambience"]
# print(zab)
# #bar.to_csv('./yelp_test4.csv')
    

 


# foo_flat = [flatten(foo) for d in foo]
# df = pd.DataFrame(foo_flat)
# print(df)


    