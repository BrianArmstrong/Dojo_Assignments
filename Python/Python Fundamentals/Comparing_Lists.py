# Assignment: Compare Lists
# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

# Your program should be able to accept and compare two lists: list_one and list_two. 
# If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." 
# Try the following test cases for lists one and two:

def ComList(list1,list2):
	if len(list1)!= len(list2):
		print "The lists are not the same"
	else:	
		for x in range (len(list1)):
			if list1[x] != list2[x]:
				print "The lists are not the same."
				break
			elif x == len(list1)-1:
				#if list[x] is the end of the list
				print x
				print "The lists are the same."
			else:
				continue
			
ComList(['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])