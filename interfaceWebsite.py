import tweetTimeline as tweet
import numpy as np
import training
import features

def grabTweets(handle):
	classifiedTweet = []
	tweets = tweet.getTweets(20, handle)
	if not tweets:
		return 0
	for i in tweets:
		fv = features.main(i)
		prediction = training.predict(fv).tolist()[0]
		preProb = training.predictProb(fv)[0][prediction]
		probPercent = round((preProb*100), 0)
		p = [i, prediction, probPercent]
		classifiedTweet.append(p)
	return (classifiedTweet)


#print(grabTweets("realDonaldTrump"))
