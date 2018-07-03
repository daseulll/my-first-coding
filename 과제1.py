name = input("한식, 중식, 일식 중 한가지를 고르세요.")
import random

if name == "한식":
    list1 = ["모래내횟집", "춘천닭갈비","잠실감자탕","삽교소곱창"]
    print(random.choice(list1))

elif name == "중식":
    list2 = ["청송각", "하오란","북경","라이"]
    print(random.choice(list2))

elif name == "일식":
    list3 = ["스시안", "수초밥","스시웨이","미소야"]
    print(random.choice(list3))
