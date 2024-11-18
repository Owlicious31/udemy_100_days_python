import random
import art
from game_data import data
run_game = True


def compare_followers():
    global score
    global topic_a
    global run_game
    if follower_count_a > follower_count_b and user_choice == "a" :
        score += 1
        print(f"You're right! Current score: {score}")
    elif follower_count_b > follower_count_a and user_choice == "b":
        score += 1
        print(f"You're right! Current score: {score}")
        topic_a = topic_b
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        run_game = False

def display_topic(topic):
    name = topic["name"]
    description = topic["description"]
    country = topic["country"]
    return f" {name}, a {description}, from {country}"

#Printing the game logo
print(art.logo)

#Picking the initial topic A
topic_a = random.choice(data)

while run_game:
    score = 0
    #Picking topic B
    topic_b = random.choice(data)

    #Making sure topic A and B are not the same.
    while topic_a == topic_b:
        topic_a = random.choice(data)

    #Gettiing follower counts
    follower_count_a = topic_a['follower_count']
    follower_count_b = topic_b['follower_count']

    #Displaying topics A and B
    print(f"Compare A: {display_topic(topic_a)}")
    print(art.vs)
    print(f"Against B: {display_topic(topic_b)} ")

    #User chooses between A and B
    user_choice = input("Who has more followers?A or B: ").lower()

    #Comparing follower counts
    compare_followers()
    print("\n")

