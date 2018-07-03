import random

winpoint = 0
losepoint = 0

while True : #무한루프. 계속 반복작업 -> 조건입력
    mine = input("scissors, rock, paper 중 하나를 고르세요.")
    Mylist = ("scissors", "rock", "paper")

    computer = random.choice(Mylist)

    print("mine :",mine ,"computer :",computer)

    try:
        if mine == computer:
            print("draw.")

        if mine == "scissors" :
            if computer == "paper" :
                winpoint += 1
                print("{} : {} You win.".format(winpoint,losepoint))

            elif computer =="rock":
                losepoint += 1
                print("{} : {} You lost.".format(winpoint,losepoint))

        if mine == "rock" :
            if computer == "scissors" :
                winpoint += 1
                print("{} : {} You win.".format(winpoint,losepoint))

            elif computer == "paper" :
                losepoint += 1
                print("{} : {} You lost.".format(winpoint,losepoint))

        if mine == "paper":
            if computer == "rock":
                winpoint += 1
                print("{} : {} You win.".format(winpoint,losepoint))

            elif computer == "scissors":
                losepoint += 1
                print("{} : {} You lost.".format(winpoint,losepoint))

    except:
        print("scissors, rock, paper 중에서 입력하세요.")
    if winpoint == 3 or losepoint == 3 :
        break;

if winpoint == 3 :
    print("Total {} : {} You win.".format(winpoint,losepoint))
if losepoint == 3 :
    print("Total {} : {} You lost.".format(winpoint,losepoint))
