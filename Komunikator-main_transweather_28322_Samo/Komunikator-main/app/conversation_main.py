#-*- coding: utf-8 -*-

#pip install nltk	
#pip install requests uuid	
#pip install googlemaps	
#pip install  dialogflow	
#pip install azure-cognitiveservices-speech	
#pip install numpy	
#pip install matplotlib	
import logging
from tkinter import *
import tkinter
import sys
import os
import matplotlib
matplotlib.use('Agg')

import random
import json
import numpy as np
import pickle
import nltk
import user_input_acquisition #zajem govora
import output_to_user
import time
import get_directions
import check_route_data_integrity
import conversation_intelligence as ci

import logging


logging.basicConfig(filename = 'logiranje.log', filemode = 'a', level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

def question_to_answer(userinput_sound):
    #get_user_input = user_input_acquisition.get_intent_from_question(userinput_sound)
    address,intent = output_to_user.talk_back(userinput_sound)
    print('intent: ', intent)
    print(type(intent))
    if intent != 'lokacija':
        return address
    #place_address = input('Address: ')
    route_data = get_directions.directions_and_weather(address)
    print(str(route_data))
    log.info("Route data: "+ str(route_data))
    all_data_received = check_route_data_integrity.get_route_data_integrity(route_data)

    weather = list(route_data[0])
    bus_info = list(route_data[1])
    
    temperature = weather[0]
    weather_desc=weather[1]
    
    if all_data_received == 0:
        return "Imamo težave pri pridobivanju podatkov, poskusite kasneje."
    elif all_data_received == 2:
        

        return "Danes na lokacijo ne pelje noben bus, pojdite peš ali z drugo obliko prevoza. Vremenski podatki: ", "Temperatura: ", temperature, "Vreme: ", weather_desc
    else:
        answer_text = ci.get_answer_text(route_data)
        suggested_path= str(answer_text) +"Vremenski podatki:\n"+ "Temperatura:"+ str(temperature)+ "\n Vreme:"+ str(weather_desc)
        return suggested_path