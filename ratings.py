"""Restaurant rating lister."""


# put your code here
import sys

def restaurant_ratings():
	filename = sys.argv[1] #creates file object, don't need to provide parameter
	open_file = open(filename) #file object
	list_of_rr = []
	for line in open_file:
		restaurants_and_ratings = line.strip().rsplit(":") #removes /n or whitespace
		list_of_rr.append(restaurants_and_ratings) #appends each line to a list
	open_file.close()
	alpha_sorted = sorted(list_of_rr)
	return(dict(alpha_sorted))


def add_user_rating():
	user_restaurant = input("Please enter a restaurant: ")
	user_rating = input("Pleae enter a rating: ")
	dic = restaurant_ratings()
	dic[user_restaurant] = user_rating
	print(dic)

add_user_rating()


