# Assignment: Scores and Grades
# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

import random
for x in range(10):
	random_num = random.randint(60,100)
	if random_num >= 60 and random_num <=69:
		print "Score: ", random_num,"; Your grade is D"
	elif random_num >= 70 and random_num <= 79:
		print "Score: ", random_num,"; Your grade is C"
	elif random_num >= 80 and random_num <=89:
		print "Score: ", random_num,"; Your grade is B"
	else:
		print "Score: ", random_num,"; Your grade is A"
	
	  
