print("Welcome to the secret Auction.")

auction_guest = {}
bidding_finish = False

while not bidding_finish:
    name = input("Enter your name : ")
    bid = int(input("Enter your bid : $"))

    auction_guest[name] = bid
    another_guest = input("Print yes if you want to continue else no : ")
    if another_guest == 'no':
        bidding_finish = True

name = max(auction_guest, key= auction_guest.get)
print(f"{name} has the higgest bid of ${auction_guest[name]}")