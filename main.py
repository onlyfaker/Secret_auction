names_and_bid_dic = {}

again='yes'
while(again=="yes"):
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))
    names_and_bid_dic[name] = bid
    again = input("Are there any other bidders? Type 'yes' or 'no': ")
    if again=='yes':
        print('\n'*100)
#todo - find the largest bidder and print it to the screeen
# for key in names_and_bid_dic:
#     if names_and_bid_dic[key]