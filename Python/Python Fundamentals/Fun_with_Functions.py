#Assignment: Fun with Functions
# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. 
# As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
def OddEven():
	for x in range(1,2001):
		if x%2 == 1:
			print "Number is ", x, "  This is an odd number."
		else:
			print "Number is ", x, "  This is an even number."
OddEven()
# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
def Multiply(list,val):
	for x in range(len(list)):
		list[x] *= val
	return list
print Multiply([2,4,6,8],5)
# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. 
# Each internal list should contain the 1's times the number in the original list.

def layered_multiples(arr):
	newarr =[]
	for x in arr:
		newarr.append([1]*x)
	print newarr
layered_multiples(Multiply([2,4,5],3))
 

