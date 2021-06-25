import tweepy
import time
from datetime import datetime

ApiKey = ""
ApiKeySecret = ""
AccessToken = ""
AccessTokenSecret = ""

auth = tweepy.OAuthHandler(ApiKey, ApiKeySecret)
auth.set_access_token(AccessToken, AccessTokenSecret)
api = tweepy.API(auth)

try:
	api.verify_credentials()

	while True:
		now = datetime.now().time()

		if now.hour == 12 and now.minute == 0 and now.second == 0:
			tweet = 'No'

			weekday = datetime.now().weekday()

			if weekday  == 0:
				image = './pictures/monday.png'
			elif weekday  == 1:
				image = './pictures/tuesday.png'
			elif weekday  == 2:
				image = './pictures/wednesday.png'
			elif weekday  == 3:
				image = './pictures/thursday.png'
			elif weekday  == 4:
				tweet = 'Yes. Stream Pink Friday for clear skin.'
				image = './pictures/friday.png'
			elif weekday  == 5:
				image = './pictures/saturday.png'
			elif weekday  == 6:
				image = './pictures/sunday.png'

			api.update_with_media(image, tweet)

			time.sleep(1)

except Exception as e:
	print(e)