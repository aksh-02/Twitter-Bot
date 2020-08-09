import tweepy
import time
from random import randint
import urllib.request
import os

def api_auth():
	api_key = ''
	api_secret_key = ''
	auth = tweepy.OAuthHandler(api_key, api_secret_key)
	token = ''
	token_secret = ''
	auth.set_access_token(token, token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	return api

def quote(num=100):
	if len(phrases) > 0:
		x = randint(0, len(phrases)-1)
		phrase = phrases[x]
	else:
		print('phrases is empty')
		return

	print('phrase :', phrase)
	phrase = phrase+' -filter:retweets'
	for tweet in tweepy.Cursor(api.search, q=phrase, tweet_mode='extended', lang='en').items(num):
		time.sleep(30)
		if tweet.in_reply_to_status_id:
			print('This tweet is a reply')
			continue
		try:
			tweet_text = '\"'+tweet.full_text+'\"'+' - '+'@'+tweet.user.screen_name
			if len(tweet_text) > 280:
				print('Length of tweet became more than 280 characters.')
				continue
			print(tweet.full_text, '\n\n')
			print(tweet_text, '\n\n')

			mids = []
			for x in tweet.entities.get('media', []):
				if x.get('type') != 'photo':
					continue
				if x.get('media_url_https'):
					urllib.request.urlretrieve(x.get('media_url_https'), "twimage.jpg")
				elif x.get('media_url'):
					urllib.request.urlretrieve(x.get('media_url'), "twimage.jpg")
				res = api.media_upload("twimage.jpg")
				mids.append(res.media_id)
			print('mids', len(mids), mids, '\n\n')

			print(tweet, '\n\n')

			tweet.favorite()
			tweet.user.follow()
			api.update_status(tweet_text, media_ids=mids)
			break
		except tweepy.TweepError as e:
			print('Some Error occurred', e)
		except Exception as e:
			print('Some Error occurred', e)
		except StopIteration:
			break
		time.sleep(10)


# Main
api = api_auth()

# Phrases
phrases = []

# Running the functions
quote()
