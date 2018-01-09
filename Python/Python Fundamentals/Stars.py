# Assignment: Stars
# Write the following functions.

# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.

def Stars(arr):
	newarr =[]
	for x in arr:
		newarr.append(["*"]*x)
	for x in newarr:
		print "".join(x)
Stars([4,6,1,3,5,7,25])

# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. 
# When a string is passed, instead of displaying *, display the first letter of the string according to the example below. 
# You may use the .lower() string method for this part.

def drawStars(arr):
	newarr =[]
	for x in arr:
		if isinstance(x,str) == True:
			x = x.lower()
			newarr.append(x[0]*len(x))

		else:
			newarr.append(["*"]*x)
	for x in newarr:
		print "".join(x)
drawStars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])