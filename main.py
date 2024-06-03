#!/usr/bin/env python3

# import required modules
import requests
import sys
import schedule
import time
import datetime
import json
import os

# define a list that can store and look through the gathered API data 
script_args=sys.argv[1:]
# test sys.argv list
# print(script_args)

# define env vars for api key and location lat/lon
api_key = os.environ.get("api_key")
lat = os.environ.get("lat")
lon = os.environ.get("lon")

#Amsterdam lat and lon details
#lat = 52.377
#lon = 4.8970

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/3.0/onecall?exclude=current,minutely,hourly,alerts&"


# define logic into function, so later it can be called by schedule for time based execution
def job():
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&lat=" + lat + "&lon=" + lon
    # check complete_url syntax
    #print(complete_url)

    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    # test successfull 200 response 
    # print(response)

    # json method of response object
    # convert json format data into
    # python format data
    # filter interested fields pop and uvi
    daily_forcast = response.json()
    rain_precentage = daily_forcast['daily'][0]['pop']
    uv_index = daily_forcast['daily'][0]['uvi']

# define conditions that would look through the list
    if "rain" in script_args:
        print("Rain information:")
        print(f"\tRain percentage {rain_precentage*100}")
        if rain_precentage>0.05:
            print(f"\t{True}")

    if "shine" in script_args:
        print("UV index:")
        print(f"\tUV index: {uv_index}")
        if uv_index>3:
            print(f"\t{True}")

# Schedule the job to run every day at 6:00 am
schedule.every().day.at("06:00").do(job)

# test schedule, by setting it to execute every 1 sec
#schedule.every().second.do(job)

while True:
    # Run pending jobs
    schedule.run_pending()
    time.sleep(1)  # Check every 1 second        
