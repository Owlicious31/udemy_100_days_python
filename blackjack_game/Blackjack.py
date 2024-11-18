import art
import  random

def tally_score(hand):
    """Returns the total value of cards in a hand."""
    score = 0
    for card in hand:
        score += card

    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = 0
        for card in hand:
            score += card

    return score

def deal_card(hand):
    """Chooses a random card from "cards" and adds it to a hand."""
    hand.append(random.choice(cards))

cards =[11,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,10 ,10 ,10]
run_game = True

while run_game:
    player_hand = []
    computer_hand = []
    player_score = 0
    computer_score = 0

    is_playing = input("Do you want to play a game of blackjack?['y' or 'n'] ").lower()
    if is_playing == "y":
        print("\n" * 20)
        print(art.logo)
        dealing_cards = True

        #DEALING THE FIRST HANDS
        for i in range(0, 2):
            deal_card(player_hand)
            deal_card(computer_hand)

        player_score = tally_score(player_hand)
        computer_score = tally_score(computer_hand)

        #CHECKING IF THE USER HAS A BLACKJACK
        if player_score == 21 and computer_score != 21:
            print(f"    Your final hand:{player_hand}, your final score:{player_score}")
            print(f"    The computer's final hand: {computer_hand}, it's final score:{computer_score}")
            print("You got a blackjack! You won!")
            break
        elif computer_score == 21:
            print(f"    Your final hand:{player_hand}, your final score:{player_score}")
            print(f"    The computer's final hand: {computer_hand}, it's final score:{computer_score}")
            print("The computer got a blackjack. You lost.")
            break

        #Main Game Loop
        while dealing_cards:
            # SHOWING THE USER'S HAND AND SCORE PLUS COMPUTER'S FIRST CARD

            print(f"    Your hand: {player_hand}, current score:{player_score}")
            print(f"    The computer's first card: {computer_hand[0]}")
            wants_more_cards = input("Type 'y' to get another card and 'n' to pass: ").lower()
            if wants_more_cards == "y":
                deal_card(player_hand)
                player_score = tally_score(player_hand)
            else:
                break
            if player_score > 21:
                break

        #HAVING THE COMPUTER DRAW CARDS
        while computer_score < 17:
            deal_card(computer_hand)
            computer_score = tally_score(computer_hand)

        #DISPLAYING FINAL SCORES
        print(f"    Your final hand:{player_hand}, your final score:{player_score}")
        print(f"    The computer's final hand: {computer_hand}, it's final score:{computer_score}")

        #CHECKING WIN/LOSE CONDITIONS
        if player_score > 21:
            print("You went over. You lost.")
        elif computer_score > 21:
            print("The computer went over. You won!")
        elif player_score == computer_score:
            print("It's a tie!")
        elif 21 - player_score < 21 - computer_score:
            print("You were closer to 21. You won!")
        elif 21 - computer_score < 21 - player_score:
            print("The computer was closer to 21. You lost.")
    else:
        break

