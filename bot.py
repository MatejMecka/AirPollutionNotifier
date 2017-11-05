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

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

auth = tweepy.OAuthHandler(clientKey, clientSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

def index_value(level):
    level = round(float(level))
    if level >= 50 and level <= 75:
        return "Среден"
    elif  level >= 76 and level < 100:
        return "Високо"
    elif level >= 101:
        return "Многу високо"


def notify(opstina,nivo,desc):
    if int(round(float(nivo))) < 50:
        print("Ниско." + nivo)
        logger.info('Ниско за {} со индекс {} на AQI скала'.format(opstina,int(round(float(nivo)))))
    else:
        if opstina == "lisice":
            message = "Еј @OpstinaAerodrom! Индексот на загаденост во Лисиче во моментот е: {}. {} според AQI индексот.".format(desc,int(round(float(nivo))))
            send_tweet(message)
        elif opstina == "kumanovo":
            message = "Еј @makraduli! Индексот на загаденост во Куманово во моментот е: {}. {} според AQI индексот.".format(desc,int(round(float(nivo))))
            ping_message = "@eko_svest @skopjesmogalarm пинг ^"
            send_tweet(message)
        else:
            message = "Еј @opstina{}! Индексот на загаденост во моментот е: {}. {} според AQI индексот.".format(opstina,desc,int(round(float(nivo))))
            print(message)
            logger.info('{} за {} со индекс {} на AQI скала'.format(desc,opstina,int(round(float(nivo)))))
            send_tweet(message)

def send_tweet(msg):
    status = api.update_status(status=msg)
    time.sleep(5)
    pingstatus = api.update_status(status=pingmessage, in_reply_to_status_id=status.id_str)

def main():
    for place in places:
        res = requests.get(url + place)
        data = json.loads(res.text)
        pollution_level = data[0]["data"]
        description = index_value(pollution_level)
        notify(place,pollution_level,description)

main()

