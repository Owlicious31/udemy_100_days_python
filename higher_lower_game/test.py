if user_choice == "a":
    if follower_count_a > follower_count_b:
        score += 1
        correct_topic = topic_a
        print(f"You're right! Current score: {score}")
        print(f"{name_a} has {follower_count_a} followers while {name_b} has {follower_count_b} followers.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        print(f"{name_b} has {follower_count_b} followers while {name_a} has {follower_count_a} followers.")
        break
if user_choice == "b":
    if follower_count_b > follower_count_a:
        score += 1
        correct_topic = topic_b
        print(f"You're right! Current score: {score}")
        print(f"{name_b} has {follower_count_b} followers while {name_a} has {follower_count_a} followers.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        print(f"{name_a} has {follower_count_a} followers while {name_b} has {follower_count_b} followers.")
        break