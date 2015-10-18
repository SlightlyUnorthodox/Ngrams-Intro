import nltk

class sentenceGenerator():

		def sentenceGenerator(toggle):
			#Test procedure (no real sentence generation)
			if toggle == 1:

			#Method1:
			elif toggle == 2:

			#Method2:
			elif toggle == 3:

			#Bad call to 'toggle'
			else:
				print "Invalid test method"

			return


		def wordReplacer(sentencePOS):
			#Picks a single word out of a sentence to replace
			
			#set random word choice start point
			num = np.random.randint(len(sen),size=1)[0]

			#process argument vectors
			sentencePOS = sentencePOS.split()			

			#loop until appropriate word is detected
			stop = "false"
			while stop == "false":
				#add extra parts of speech if necessary
				if sentencePOS[num] == "adjective" || sentencePOS[num] == "noun" || sentencePOS[num] == "verb":
					stop = "true"
				else:
					#if not correct part of speech move to next word
					num = (num + 1) % len(sentencePOS)

			#return word replacement index
			return num
