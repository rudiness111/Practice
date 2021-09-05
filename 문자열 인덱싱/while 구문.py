treehit = 0
while treehit < 10:
    treehit = treehit +1
    print("나무를 %d번 찍었습니다." % treehit)
    if treehit == 10:
        print("나무 넘어갑니다.")

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피 드릴께요.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 내일 다시 와주세요.")
        break

a = 0
while a < 10:
    a = a+1
    if a % 2 == 0:
        continue
    print(a)
