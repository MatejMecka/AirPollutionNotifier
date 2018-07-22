# -*- coding: utf-8 -*-

import requests
import json
import tweepy
import time
import sys
from config import *
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

handler = logging.FileHandler(log_file)
handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

auth = tweepy.OAuthHandler(clientKey, clientSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

count = 0


def index_value(level):
    """
    Converts the Index Value to a meaningful String describing the level of pollution
    based on Europeans AQI Index Level

    https://en.wikipedia.org/wiki/Air_quality_index#Europe

    :param level: The AQI Index from the pollution station
    :return: String, Describtion of Pollution level
    """
    level = round(float(level))
    if level >= 50 and level <= 75:
        return "Среден"
    elif level >= 76 and level <= 100:
        return "Високо"
    elif level >= 101:
        return "Многу високо"


def notify(opstina, nivo, desc):
    """
    Checks if it's Polluted and prepares the message for it to be tweeted

    :param opstina: The Municipality where the pollution is
    :param nivo: The pollution level for the Station
    :param desc: The Description of the pollution level
    """
    if int(round(float(nivo))) < 50:
        print("Ниско." + nivo)
        logger.info('Ниско за {} со индекс {} на AQI скала'.format(opstina,int(round(float(nivo)))))
    else:
        message = "Еј {}! Индексот на загаденост во моментот е: {}. {} според AQI индексот.".format(
            opstina, desc, int(round(float(nivo))))
        print(message)
        if opstina == "karpos" or opstina == "centar" or opstina == "rektorat" or opstina == "lisice" or opstina == "gazibaba" or opstina == "miladinovci" or opstina == "mrsevci":
            ping_message = "Eko_Svest, Skopje Smog Alarm? ^"
            send_tweet(message)
        else:
            send_tweet(message)


def send_tweet(msg):
    """
    Tweets the Message from notify
    
    :param msg: The Tweet Content
    """
    status = api.update_status(status=msg)
    time.sleep(5)
    #pingstatus = api.update_status(status=pingmessage, in_reply_to_status_id=status.id_str)


def main():
    for place, person in places.items():
        print(place)
        res = requests.get(url + place)
        data = json.loads(res.text)
        pollution_level = data[0]["data"]
        description = index_value(pollution_level)
        notify(person, pollution_level, description)


main()
