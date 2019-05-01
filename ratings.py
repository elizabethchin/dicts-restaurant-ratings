"""Restaurant rating lister."""


# put your code here
import sys

def restaurant_ratings(file):

	file = sys.argv[1]
	

	for line in open(file):
		restaurants_and_ratings = line.split(":")
	

	length = len(restaurants_and_ratings)
	i = 0
	restaurant_dict = {}
	while i < length - 1:
		restaurant_dict[restaurants_and_ratings[i]] = restaurants_and_ratings[i + 1]
	return restaurant_dict

print(restaurant_ratings("scores.txt"))

