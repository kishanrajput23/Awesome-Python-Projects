#Ask a user for a list of 3 friends.
#For each friend of user We'll tell whether he/she is nearby.
#For every nearby friend we'll save their names in "nearby_friends.txt0".
 
friends = input("Enter names of 3 friends: ").split(",")
with open("people.txt", "r") as people:
    nearby_people = [line.strip() for line in people.readlines()] # With open automatically opens and closes the file.

my_friend = set(friends)
nearby = set(nearby_people)
friends_nearby_set = my_friend.intersection(nearby)

with open("nearby_friends.txt", "w") as nearby_friends_file:
    for friend in friends_nearby_set:

        nearby_friends_file.write(f"{friend}\n")
        print(f"{friend} is nearby, let's meet up")

nearby_friends_file.close()

