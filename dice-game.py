import requests
import random
import math
myHook = ""
def send_discord(msg, url: str):
    if not url:
        return
    data = {"content": f"{msg} "}
    requests.post(url, json=data)

def die(i):
    return "\u2680\u2681\u2682\u2683\u2684\u2685"[i - 1]

def add_dice(i, j):
    print("Die:",die(i), die(j))
    print("Results: ",i + j)
    
def roll_dice():
    one = random.choice(dice_num)
    two = random.choice(dice_num)
    result = one + two
    roll_result.append(result)
    return one, two

def roll_results():
    avg_results = sum(roll_result) / len(roll_result)
    print("List of Results: ",roll_result)
    print("Avg:",avg_results)

def run_loop():
    while True:
        x = input("Play this game? Y/N: ")
        if x == "y" or x == "yes":
            roll_one, roll_two = roll_dice()
            add_dice(roll_one, roll_two)

        else:
            print("you didnt type y or yes")
            break

if __name__ == "__main__":
    result = 0
    roll_result = []
    dice_num = [1,2,3,4,5,6]
    run_loop()
    roll_results()
    send_discord(roll_results, myHook)
