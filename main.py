import random
import os
import time
from art import logo


auction_items = {
    "Gaming Laptop": 1000,
    "Iphone 17 Pro Max": 600,
    "Art Painting": 1200,
    "Bluetooth Speaker": 500,
    "Rolex": 1500,
    "Gaming PC Set": 500
}


def clrscr():
    """Clears the screen.
    When running in the output console this doesn't work.
    Fix: Go to 'Run' -> Edit Configuration -> Select Python in the left sidebar.
    Then, Modify Option -> Emulate terminal in output console
    Lastly, from the dropdown, select 'module' -> enter the name of your 'main.py' file.
    Note: This is for Pycharm 😉
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def select_random_items(items) -> tuple:
    """
    Select random auction item.
    :param items: use the auction_items dict
    :return: tuple for identifying item and its price
    """
    item = random.choice(list(items.keys()))
    base_price = items[item]
    del items[item]

    return item, base_price


def get_bids(item) -> dict:
    """Get the bids of the user and return it as a dict."""
    continue_bidding = True
    bids = {}
    while continue_bidding:
        print(logo)
        print("Welcome to the Bidding!")
        print(f"Item: {item[0]}")
        print(f"Base bidding price: {item[1]}")

        name = input("Enter your name (or type 'pass' if you don't want to bid'): ").lower()
        if name == "pass":
            clrscr()
            continue
        else:
            while True: #loop until a valid bid amount is entered
                try:
                    bid_amount = float(input(f"Hi, {name}. What is your bid for {item[0]}: "))
                    if bid_amount <= item[1]:
                        print(f"Amount must be higher than '₱{item[1]:,.2f}'.")
                    else:
                        bids[name] = bid_amount #assign user and their bid amount
                        clrscr()
                        break #escapes the inner loop when a valid bid amount is entered
                except ValueError: #avoid program crashing because of wrong input
                    print("Invalid bid. Please enter an amount.")

        other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if other_bidders == "no":
            continue_bidding = False

    return bids

def find_highest_bid(bids) -> tuple:
    """Get the user with the highest bid."""
    return max(bids, key=bids.get), bids[max(bids, key=bids.get)]


while auction_items:
    bid_item = select_random_items(auction_items)
    bid = get_bids(bid_item)
    highest_bidder = find_highest_bid(bid)

    print(f"The winner is {highest_bidder[0]} with a bid amount of ₱{highest_bidder[1]:,.2f}")
    time.sleep(3) #to display the winner first before clearing the screen
    clrscr()
    if auction_items == {}: #if there are no more items, exit the loop
        break