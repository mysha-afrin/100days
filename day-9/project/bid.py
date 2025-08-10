
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
