from nltk.corpus import stopwords
import nltk


def removeStopHash(string):
	stop = set(stopwords.words("english")) #create set of stop words to check
	new = ""
	text = nltk.word_tokenize(string)	
	for word in string.split(): 
		if word in stop:
			continue #current word in string is a stop word
		if word[0] == '#':
			continue
		else:
			new += word + " " #not a stop word append
	return(new)
