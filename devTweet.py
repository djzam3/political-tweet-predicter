import tweetTimeline as tweet
import features
import numpy as np
import training

"""Used just to grab training sets"""
def main():
	while True:
		try:
			cnt = int(input("How many tweets: "))
			break
		except ValueError:
			print("Must be an integer")
	f = open("statements.txt", 'a') #open for appending
	twitterHandle = input("Persons twitter handle: ")
	tweets = tweet.getTweets(cnt, twitterHandle)

	if not tweets:
		return #Cant fetch tweets

	for i in tweets:
		print(i)
		c = input("Is this verifiable?: ")
		if c == '-1': #do not add to list
			continue
		f.write(c + " " + i + '\n')
	f.close()

def dataset3FV():
	f = open("tweet-ds-012.txt", "r")
	data = []
	target = []
	for line in f:
		target.append(int(line[0])) # 0 or 1
		data.append(features.main(line[2:]))
	data = np.array(data)
	target = np.array(target)
	f.close()
	print(data)
	print(target)
	return(data, target)

def dataset2FV():
	f = open("tweet-ds-01.txt", "r")
	data = []
	target = []
	for line in f:
		target.append(int(line[0])) # 0 or 1
		data.append(features.main(line[2:]))
	data = np.array(data)
	target = np.array(target)
	f.close()
	print(data)
	print(target)
	return(data, target)

def showSVM():
	info = dataset3FV()
	training.show(info[0], info[1])


def SVM():
	info = dataset3FV()
	training.trainSVM(info[0], info[1])

def NB():
	info = datasetFV()
	training.trainNB(info[0], info[1])
	print(training.predict([0, 0, 0, 0, 1]))

def CM():
	info = datasetFV()
	training.train_conf(info[0], info[1])

if __name__ == "__main__":
	#NB()
	#SVM()
	#CM()
	#showSVM()
	#datasetFV()
	#print(training.predict([0, 0, 0, 0, 2]))
	#print(training.predictProb([0, 1, 0, 0, 0]))
