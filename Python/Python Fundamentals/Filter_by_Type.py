# Assignment: Filter by Type

# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"
def intGreatLess(int):
	if int >= 100:
		print "That's a big number!"
	else:
		print "That's a small number"
intGreatLess(45)
# String
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."
def LongShort(sentence):
# string = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
	if len(sentence)>=50:
		print "Long sentence."
	else:
		print "Short sentence"
LongShort("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
# List
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
def BigShort(list):
	if len(list)>=10:
		print "Big list!"
	else:
		print "Short list."
BigShort(['name','address','phone number','social security number'])
