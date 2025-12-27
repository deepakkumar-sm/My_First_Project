# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
 
from art1 import logo

print(logo)

# bidder_name = input("What is your name?: ")
# bidder_bid = int(input("What is your bid?: $"))

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

dict = {}
continue_bidding = True

while continue_bidding:
    bidder_name = input("What is your name?: ")
    bidder_bid = int(input("What is your bid?: $"))
    dict[bidder_name] = bidder_bid
    bidder_available = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    if bidder_available == "no":
        continue_bidding = False
        find_highest_bidder(dict)
    elif bidder_available == 'yes':
        print("\n" * 200)





# print(dict)
# find_highest_bidder(dict)

