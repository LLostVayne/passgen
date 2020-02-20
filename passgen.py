import random
import string


def RandomPass():
	min_pass_len = 12
	while True:
		try:
			pass_len = int(input("How long should the password be?(MIN {}): ".format(min_pass_len)))
			if pass_len < min_pass_len:
				print("Needs to be higher than 12.")
			else:
				break
		except ValueError:
			print("Needs to be a number.")
	combination = string.ascii_letters + string.digits + string.punctuation
	password = "".join([random.choice(combination) for i in range(pass_len)])
	return password


def HumanReadablePass(x):
	letter_changes = {'e':'3', 'i':'1', 'o':'0', 'a':'4', 's':'$'}
	special_chars = '~!@#^*-_'
	if x == 'words_list':
		with open("words_list.txt", 'r') as file:
			text = [line.rstrip() for line in file]
			file.close()
		password = [random.choice(text).lower() for i in range(3)]#Change number for more/less words
	else:
		password = []
		while 1:
			word = str(input("Enter word you want in your password[done() to exit]: "))
			if word.lower() == 'done()' or word.lower() == 'exit()':
				break
			else:
				password.append(word)
	for word in password:
		replica_word = word
		random_letter = random.choice(word)
		replica_word = replica_word.replace(random_letter, random_letter.upper())#Capitalazing a random letter
		for letter in word:
			if letter in letter_changes:
				replica_word = replica_word.replace(letter, letter_changes[letter])
		password[password.index(word)] = replica_word
	password = random.choice(special_chars).join(password)#Connecting the words
	return password


choice = str(input("What do you want your password to be?\n"
				   "[A] Random letters/numbers/punctuations\n"
				   "[B] Random human readable password generated from a word list\n"
				   "[C] Human readable password inserted by user\n>>"))


if choice.lower() == 'a':
	print(RandomPass())
elif choice.lower() == 'b':
	print(HumanReadablePass('words_list'))
elif choice.lower() == 'c':
	print(HumanReadablePass('inserted'))
else:
	print("Wrong input")
	quit()