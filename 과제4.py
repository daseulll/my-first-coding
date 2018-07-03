# for i in range(5):
#     for j in range(5):
#         if j <= i :
#             print("*", end="")
#     print()

# for i in range(5):        # 5번 반복. 세로 방향
#     for j in range(5):    # 5번 반복. 가로 방향
#         if j <= i:                # 세로 방향 변수만큼
#             print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#     print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
#                # (print는 출력 후 기본적으로 다음 줄로 넘어감)


# for a in range(1, 6):
#     # for b in range (1, 6):
#     #     print()
#
# for a in range(1, 6):
#     print("1" * a + "0"*(5-a))

# for a in range(1, 6):
#     a = a - 3
#     if a < 0 :
#         a = -a
#     print("0" * a + "1"*(5 - a * 2) + "0" * a)

for a in range(1, 6) : # a=> 2,1,0,1,2
    a = a - 3
    if a < 0 :
        a = -a
    print("0" * a + "1" * (5 - a * 2) +"0" * a)
