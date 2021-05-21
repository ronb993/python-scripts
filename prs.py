import random
myList = ["Rock", "Scissor", "Paper"]
myScore = 0
cScore = 0

while (myScore != 3 and cScore != 3):
    print("Player Score =:", myScore, "Computer Score =:", cScore)
    random.shuffle(myList)
    x = myList[0]

    myHand = input("Rock, Paper, or Scissor? :")

    if (myHand == "Rock" and x == "Paper"):
        print("paper beats rock, computer wins")
        cScore += 1
    elif (myHand == "Rock" and x == "Scissor"):
        print("rock beats scissor, you win")
        myScore += 1

    elif (myHand == "Rock" and x == "Rock"):
        print("Rock and Rock, is a tie")

    elif (myHand == "Paper" and x == "Rock"):
        print("Paper beats rock, you win!")
        myScore += 1

    elif (myHand == "Paper" and x == "Scissor"):
        print("Scissor beats paper, you lose")
        cScore += 1

    elif (myHand == "Paper" and x == "Paper"):
        print("Paper & Paper, stale mate")

    elif (myHand == "Scissor" and x == "Scissor"):
        print("scissor and scissor, stale mate!")

    elif (myHand == "Scissor" and x == "Paper"):
        print("scissor beats paper, you win!")
        myScore += 1

    elif (myHand == "Scissor" and x == "Rock"):
        print("Rock beats scissor, you lose!")
        cScore += 1
    else:
        print("not a valid response")

print("Total Score - Player1:",myScore," Computer:",cScore)