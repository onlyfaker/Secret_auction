from art import LOGO
print(LOGO)
#In case of the more than one same highest bidsL: First bid received wins
def highest_bidder():
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bidder_ask = bids[bidder]
        if bidder_ask > highest_bid:
            highest_bid = bidder_ask
            winner = bidder
    print(f"The winner is {winner} with the highest bid {highest_bid}")
#or
#highest_value_key = max(bids, key=bids.get)
#bids[highest_value_key] - gives the highest value..


bids = {}
ongoing=True

while(ongoing):
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))
    bids[name] = bid
    again = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if again=='no':
        ongoing=False
        highest_bidder()
    elif again=='yes':
        print('\n' * 20)



