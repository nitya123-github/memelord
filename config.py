import json
import os
import tweepy
import praw
import json
import time
import datetime
import re
import sys
import requests
import mysql.connector as mysql
from dotenv import (load_dotenv, find_dotenv)
load_dotenv(find_dotenv())

# Replace the values in the fields below with your own info
#[DATABASE]
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
database = os.getenv("MYSQL_DATABASE")

#[TWITTER]
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET_KEY")
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
db = mysql.connect(user=user, passwd=password, host=host, database=database)
with open("twitter/twitter-accounts.json") as f:
    data = json.load(f)
    twitterAccounts = data['twitterAccounts']

#[BOT]
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

#[IMAGEUPLOAD]
client_id = os.getenv("IMGUR_CLIENT_ID")
imgur_upload_url = "https://api.imgur.com/3/image"

#[REDDIT]
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
