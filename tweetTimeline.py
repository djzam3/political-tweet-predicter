import twitter

def establishConnection():
    """
    Set up connection to twitter API
    :return: 
    """
    api = twitter.Api(consumer_key='px2i4p3dmPfpz9T2tLAlGb3g2',
                      consumer_secret='dMmRv7CIp6N3OQ11TEjnFLuCuTJUZR4vIIA92LWh8MLPBUwh17',
                      access_token_key='846900989672112128-9QlyvdDLbTfAwWroqvH81w0BmiYU9nN',
                      access_token_secret='nPH1EeZwnT7Yk9KkBmnlblKwxZj437mTy8WESpwCHngCq', tweet_mode='extended')
    
    return api

def getTweets(count, twitterHandle):
	"""
	:param count: Amount of tweets wanting to retieve
	:return: List of tweets 
	"""
	api = establishConnection()
	
	try:
		stats = api.GetUserTimeline(screen_name=twitterHandle, count=count, include_rts=False)
	except:
		print("Error: Unable to fetch tweets from specified user")
		return 0
	
	return ([s.full_text for s in stats])
		

	
