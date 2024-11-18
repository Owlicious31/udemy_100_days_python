# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo2)


should_continue = True
names_and_bids = {}

while should_continue:
    name = input("What is your name?").lower()
    bid = int(input("What is your bid? $"))
    other_bidders = input("Is there anyone else who would like to bid?(Yes or No)\n").lower()

    names_and_bids[name] = bid
    if other_bidders == "no":
        should_continue = False
    else:
        print("\n" * 100)

highest_bid = 0
winner = ""
for name in names_and_bids:
    if names_and_bids[name] > highest_bid:
        highest_bid = names_and_bids[name]

for name in names_and_bids:
    if names_and_bids[name] == highest_bid:
        winner += name

print(f"The winner is {winner} with a bid of {highest_bid}!")
