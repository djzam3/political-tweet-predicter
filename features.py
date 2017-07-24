import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import numpy as np
import stringStand as stand

def getFeatures(text):
	opinionSet = ('think', 'want', 'seems', 'my', 'personally', 'maybe', 'opinion', 'imagine', 'convinced', 'my', 'recommend', 'believe', 'hope', 'should', 'thought', 'need')
	fv = np.array([0, 0, 0, 0, 0])
	for i in range(len(text)):
		if text[i][1] == 'JJS':  # Superlative
			fv[0] += 1

		if text[i][1] == 'CD':  # Numeral
			fv[1] += 1

		if (text[i][1] == 'JJR') or (text[i][1] == 'RBR'): #comprative
			fv[2] += 1

		if text[i][0] in opinionSet:
			fv[3] += 1

	for (w1, t1), (w2, t2) in nltk.bigrams(text):
		if (t1 == 'PRP' or t1 == 'NN' or t1 == 'NNP' or t1 == 'NNS') and (t2 == 'VBD'): # Noun/pronoun + verb
			fv[4] += 1  
		
	return fv #features



def tagHelp(text):
	#text = getTok(text)
	for i in range(len(text)):
		print(text[i][0])
		print(nltk.help.upenn_tagset(text[i][1]))

def getTok(text):
	tok = TweetTokenizer(strip_handles=True, reduce_len=True)
	return tok.tokenize(text) #tokenize

def getTag(text):
	stopText = stand.removeStopHash(text)
	tokText = stopText.split()
	
	text = nltk.pos_tag(tokText) #tag
	#tagHelp(text)	
	return text

def main(tweet):
	text = getTag(tweet)
	#tagHelp(text)
	fv = getFeatures(text)
	return fv #numpy array of feature extraction

