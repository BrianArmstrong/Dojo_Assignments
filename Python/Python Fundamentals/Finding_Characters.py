# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

def findChar(list, char):
	new_list = [] 
	for x in list:
		if x.find(char) != -1:
			new_list.append(x)
	print new_list
findChar(['hello','world','my','name','is','Anna'], "o")	
