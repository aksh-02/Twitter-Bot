import tweepy
import time
from random import randint
import urllib.request

def api_auth():
	api_key = ''
	api_secret_key = ''
	auth = tweepy.OAuthHandler(api_key, api_secret_key)
	token = ''
	token_secret = ''
	auth.set_access_token(token, token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	return api


def tweet_once():
	if len(tweets_list) > 0:
		x = randint(0, len(tweets_list)-1)
		tweet = tweets_list[x]
	else:
		print('tweets_list is empty')
		return

	try:
		print(tweet)
		api.update_status(tweet)
	except tweepy.TweepError as e:
		print("Couldn't post.", e)


# Main
api = api_auth()


# Random Tweets
tweets_list = []

# Running the functions
tweet_once()


