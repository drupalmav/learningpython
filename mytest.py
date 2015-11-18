import tweepy

CONSUMER_KEY = 'qdmSDjx2zpMRJY8IJzZbgVaY3'
CONSUMER_SECRET = 'dzy2OF4Cby4UTkV5HmfcjQC4ah6fMSXVv5mYicQe0IYlshx7KR'
ACCESS_TOKEN = '25001837-2vzEfgublXhkTJrKCiF7uXy3FqmuC0tfCNXl88yus'
ACCESS_TOKEN_SECRET = 'v5J0hhedpKfBViH5IFPMiR2dJNY0ilZMxy3CmYlvFGusu'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "Testing!"
#api.update_status(status=status)

#Get Tweets from HOME of user's page
'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
    print "\n"
'''

#Get the User object for twitter...
user = api.get_user('realDonaldTrump')

print user.screen_name
print user.followers_count
for friend in user.friends():
   print friend.screen_name


