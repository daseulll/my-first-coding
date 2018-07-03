import random
rock = "바위"
scissors = "가위"
paper = "보"

RSP_list = (rock, scissors, paper)

win_count = 0
lose_count = 0

while win_count < 3 and lose_count <3 :
    User_choice = input("{}, {}, {} 중 선택하세요.".format(rock,scissors,paper))

    computer_choice = random.choice(RSP_list)
    if User_choice not in RSP_list :
        print("가위, 바위, 보 중에서 선택해주세요.")

    elif User_choice == computer_choice :
        print ("비겼습니다.")

    elif ((User_choice == scissors and computer_choice == paper)
        or (User_choice == rock and computer_choice == scissors)
        or (User_choice == paper and computer_choice == rock)) :
       win_count += 1
       print("{} : {} 이겼습니다".format(win_count,lose_count))

    else :
         lose_count += 1
         print("{} : {} 졌습니다.".format(win_count,lose_count))

if win_count == 3 :
    print("최종 결과 {} : {} 이겼습니다.".format(win_count,lose_count))

else :
    print("최종 결과 {} : {} 졌습니다.".format(win_count,lose_count))
