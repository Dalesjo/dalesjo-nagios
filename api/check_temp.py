#!/usr/bin/python3
import urllib.request, json 
import argparse
import sys
import json
import os

# Get arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--thermometer", required=True, help="id of thermometer to test",type=str)
ap.add_argument("-T", "--maxTemperature", default=100, help="Max temperature before warning",type=float )
ap.add_argument("-M", "--maxHumidity", default=100, help="Max humidity before warning",type=float )
ap.add_argument("-t", "--minTemperature", default=-100, help="Minimum temperature before warning",type=float )
ap.add_argument("-m", "--minHumidity", default=0, help="Minimum humidity before warning",type=float )
args = vars(ap.parse_args())


url = "https://temperature.dalesjo.com/api/Thermometer?ThermometerId="+ args["thermometer"]
with urllib.request.urlopen(url) as response:
    
    if(response.code != 200):
        print("Thermometer "+ args["thermometer"] +" does not exist")
        sys.exit(3)
    
    data = json.loads(response.read().decode())
    stats = "TEMPERATURE="+ str(data["temperature"]) +";"+ str(args["minTemperature"]) +";"+ str(args["maxTemperature"]) +" HUMIDITY="+ str(data["humidity"]) +";"+ str(args["minHumidity"]) +";"+ str(args["maxHumidity"])

    if(data["temperature"] > args["maxTemperature"]):
        print("Temperature to high ("+ str(data["temperature"]) +") | "+ stats)
        sys.exit(1)

    if(data["temperature"] < args["minTemperature"]):
        print("Temperature to low ("+ str(data["temperature"]) +") | "+ stats)
        sys.exit(1)

    if(data["humidity"] > args["maxHumidity"]):
        print("Humidity to high ("+ str(data["humidity"]) +") | "+ stats)
        sys.exit(1)

    if(data["humidity"] < args["minHumidity"]):
        print("Humidity to low ("+ str(data["humidity"]) +") | "+ stats)
        sys.exit(1)   

    print("Temperature is "+ str(data["temperature"]) +" ("+ str(data["humidity"]) +"%) | "+ stats)
    sys.exit(0)                       