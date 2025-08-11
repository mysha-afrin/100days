from art import logo
print(logo[0])
bid = {}


continue_bidding = True
while continue_bidding:
    bidder = input("Enter your name: ")
    money = int(input("Enter your bid amount: $"))
    bid[bidder] = money
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' :\n").lower()
    if should_continue == "no":
        continue_bidding = False
    elif should_continue == "yes":
        continue_bidding = True
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")