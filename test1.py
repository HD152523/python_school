import time
import random

human_num = int(1)

print("당신은 나무꾼입니다.\n나무를 찍어봅시다.")

bear_num = random.randrange(1, 11)


def run():
    print("당신은 1번을 선택하셨습니다.")
    print("최선을 다해 뛰세요!!!")
    for num in range(1, 4):
        print("더 " * num + "빨리~")
        time.sleep(1)
    chase_num = random.randrange(2)
    if chase_num == 0:
        print("곰에게 잡혔네요. ㅠㅠ")
    elif chase_num == 1:
        print("휴~ 무사히 도망쳤네요. ^^")


def fight():
    print("fight")


while human_num <= 10:
    print("나무를 " + str(human_num) + "번 찍었습니다.")
    human_num += 1
    time.sleep(1)

    if human_num == bear_num:
        print("나무를 찍던 중 당신은 큰 곰을 만납니다!!")
        print("도망칠까요?(1) 싸울까요?(2)")
        human = int(input())
        if human == 1:
            run()
            break
        elif human == 2:
            fight()
            break
    else:
        continue
