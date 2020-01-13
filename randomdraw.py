"""
A simple python file for randomly selecting names from a dictionary list
Names drawn are considered winners of an art raffle.
"""

import random

def main(user_dict, limit):
    banner = ["++++++++++++++++++++++++++++++",
              "+ Art Raffle Random Selector +",
              "++++++++++++++++++++++++++++++"]
    for row in banner:
        print(row)
    print()
    while True:
        winners = draw_winner(user_dict, limit)
        output(winners)
        catcher = input("Again? (Press any key to quit): ")
        if catcher != "":
            print("\nQuitting...\n")
            break
        else:
            print("\nContinuing...\n")
        
def draw_winner(user_dict, limit):
    count = 0
    selector = None
    used_int = []
    length = len(user_dict)
    winners = []
    while count < limit:
        count += 1
        selector = random.randint(1, length)
        if selector in used_int:
            while selector in used_int:
                selector = random.randint(1, length)
        winners.append(user_dict[selector])
        used_int.append(selector)
    return winners

def output(final):
    message = "Results of the draw:"
    print(len(message) * "=")
    print(message)
    count = 1
    for winner in final:
        print(str(count) + ") " + winner)
        count += 1
    print(len(message) * "=")

user_dict = {1:"", 2:"",
             3:"", 4:"",
             5:"", 6:"",
             7:"", 8:"",
             9:"", 10:"",
             11:"", 12:"",
             13:"", 14:"",
             15:"", 16:"",
             17:"", 18:"",
             19:"", 20:""}
win_count = 2

main(user_dict, win_count)
