"""
Name:	Dean Fleming
Email:	<deanf1@umbc.edu>
Class:	CMSC 471 - 01
 
Homework 2
Converts two three-letter words from one to the other by switching one
letter at a time, each step in between being real words.
"""

from random import randint

"""
Reads the input file and creates a list of words from it

Returns:	list of words
"""
def readWords():

	# opens the word list file
	try:
		wordFile = open("words.txt", 'r');
	except IOError:
		print "Error: words.txt not found"
		exit()

	# gets all the words, splitting by all white space to be safe
	wordList = []
	for line in wordFile:
		for word in line.split():
			wordList.append(word)

	return wordList

"""
Validates inputted words to make sure they are in the list

word:		the inputted word
wordList:	the list of all legal words

Returns:	True or False depending on if the word is valid or not
"""
def validate(word, wordList):

	if not (word in wordList):
		print "Error with word \"%s\": Must be found in words.txt" % word
		return False

	return True

"""
Main method
"""
def main():
	
	wordList = readWords()

	print ("DOGCAT: Enter 2 three-letter words, or leave blank to "
	+ "have them chosen for you")
	
	# input validation loop
	validInput = False
	while (not validInput):
		startWord = raw_input("Enter the word to start from: ").strip().lower()
		endWord = raw_input("Enter the word to end at: ").strip().lower()

		startValid = False
		endValid = False

		# choses a start word if left empty, or validates it if it was chosen
		if (startWord == ""):
			startWord = wordList[randint(0, len(wordList) - 1)]
			print "Generated start word: \"%s\"" % startWord
			startValid = True
		else:
			startValid = validate(startWord, wordList)

		# choses an end word if left empty, or validates it if it was chosen
		if (endWord == ""):
			endWord = wordList[randint(0, len(wordList) - 1)]
			print "Generated end word: \"%s\"" % endWord
			endValid = True
		else:
			endValid = validate(endWord, wordList)

		# exits the loop if both words are valid
		if (startValid and endValid):
			validInput = True

main()