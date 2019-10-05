import random

def main(user_dict):
    banner = ["++++++++++++++++++++++++++++++",
              "+ Art Raffle Random Selector +",
              "++++++++++++++++++++++++++++++"]
    for row in banner:
        print(row)
    print()
    while True:
        winners = draw_winner(user_dict)
        output(winners)
        catcher = input("Again? (Press any key to quit): ")
        if catcher != "":
            print("\nQuitting...\n")
            break
        else:
            print("\nContinuing...\n")
        
def draw_winner(user_dict):
    count = 0
    selector = None
    used_int = []
    length = len(user_dict)
    winners = []
    while count < 3:
        count += 1
        selector = random.randint(1, length)
        if selector in used_int:
            temp = selector
            while selector == temp:
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

main(user_dict)
