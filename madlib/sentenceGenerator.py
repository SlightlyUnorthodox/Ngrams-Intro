import nltk
import numpy as np

#class sentenceGenerator():

def generateSentence(toggle,size):
	#Toggle selects which method to use
	#Size defines number of sentences to create (functionality to be added)

	#Test procedure (no real sentence generation)
	if toggle == 1:
		sentence = "This is a test sentence"
		sentencePOS = "pronoun verb article adjective noun"
		return (sentence,sentencePOS)
	
	#Method1:
	elif toggle == 2:

	#BUILD METHOD 2 HERE



	#END METHOD 2
		return(sentence,sentencePOS)
	
	#Method2:
	elif toggle == 3:

	#BUILD METHOD 3 HERE 



	#END METHOD 3
		return(sentence,sentencePOS)
	#Bad call to 'toggle'
	else:
		print "Invalid test method"

	return ("null","null")


def wordReplacer(sentencePOS):
	#Picks a single word out of a sentence to replace
			
	#process argument vectors
	sentencePOS = sentencePOS.split()			

	#set random word choice start point
	num = np.random.randint(len(sentencePOS),size=1)[0]

	#loop until appropriate word is detected
	stop = "false"
	while stop == "false":
		#add extra parts of speech if necessary
		if sentencePOS[num] == "adjective":
			stop = "true"
		elif sentencePOS[num] == "verb":
			stop = "true"
		elif sentencePOS[num] == "noun":
			stop = "true"
		else:
			#if not correct part of speech move to next word
			num = (num + 1) % len(sentencePOS)

	#return word replacement index
	return num
