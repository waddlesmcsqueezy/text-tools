#This function takes user input via the cmd window

def command():
	return input("Enter a word: ") #takes input from user

#This function takes use input as "word" then converts it into pig latin form and then prints it

def vowelCounter():
	word = str(command()) #Use command() to take user input and assign that to "word"
	original_word = word #saves the original word user wants to convert for later use
	word = list(word) #convert "word" to an array of char's
	first_letter = word[0:1] #uses slicing to extract first letter in "word"
	first_letter = ''.join(first_letter) #converts first_letter from a list to a string
	del word[0] #deletes the first object in list "word"
	word = ''.join(word) #converts "word" from list to string
	word = word + "-" + first_letter + "ay" #makes word the pig latin version of itself
	print("Your word, " + original_word + ", " + "is " + word + " in Pig Latin.") #print

vowelCounter() #run the main function