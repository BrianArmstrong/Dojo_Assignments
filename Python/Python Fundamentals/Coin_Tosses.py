# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. 
# Your function should print how many times the head/tail appears.

import random
def CoinToss():
	h = 0
	t = 0
	for x in range(1,1001):

		coin = random.randint(0,1)
		
		if coin == 0:
			h += 1
			print "Attempt #"+str(x)+":", " Throwing a coin... It's a head! ... Got", h, "head(s) so far and ", t, "tail(s) so far"

		else:
			t += 1
			print "Attempt #"+str(x)+":", " Throwing a coin... It's a tail! ... Got", h, "heads(s) so far and ", t, "tail(s) so far"
print "Ending the program, thank you!"
CoinToss()