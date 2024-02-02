import os

auction = []
new_bidders = True
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |    Secret     | | ''-.
                          |       |_| |_   Auction   _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

def find_highest_bidder(auction):
    highest_bidder = ""
    highest_bid = 0
    for bidder in auction:
        #print(bidder["bid"])
        if bidder["bid"] > highest_bid:
            highest_bidder = bidder["name"]
            highest_bid = bidder["bid"]
    print(f"the winner was {highest_bidder} with a bid of ${highest_bid}")

while new_bidders:
    new_bidder = {}
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    new_bidder["name"] = name
    new_bidder["bid"] = bid
    auction.append(new_bidder)
    add_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").upper()
    if add_bidder == "YES":
        os.system('cls')
    else:
        find_highest_bidder(auction)
        new_bidders = False

#print(auction)




