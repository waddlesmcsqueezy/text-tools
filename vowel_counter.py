#This function takes user input via the cmd window

def command():
	return input("Enter a word: ")

#This function counts the number of vowels in variable "word" and then prints them

def vowelCounter():
	word = str(command()) #Use command() to take user input and assign that to "word"
	word = list(word) #convert "word" to an array of char's
	vowel_count = str(word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')) #Get number of instances of a e i o & u in array "word"
	print("Your word(s) contained " + vowel_count + " Vowel(s).") #print final sum of vowels

vowelCounter() #run the main function