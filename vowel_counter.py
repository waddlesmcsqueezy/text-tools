def command():
	return input("Enter a word: ")
def vowelCounter():
	word = str(command())
	word = list(word)
	vowel_count = str(word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u'))
	print("Your word(s) contained " + vowel_count + " Vowel(s).")

vowelCounter()