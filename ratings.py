"""Restaurant rating lister."""


# put your code here
import sys

def restaurant_ratings():

	filename = sys.argv[1]
	open_file = open(filename) #file object

	list_of_rr = []
	for line in open_file:
		restaurants_and_ratings = line.strip().rsplit(":")
		list_of_rr.append(restaurants_and_ratings)
	open_file.close()

	alpha_sorted = sorted(list_of_rr)

	return(dict(alpha_sorted))


print(restaurant_ratings())