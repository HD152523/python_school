import time
import random

# 초기 시작 화면
human_num = int(1)
bear_num = random.randrange(1, 11)

print("당신은 나무꾼입니다.\n나무를 찍어봅시다.")


# 도주 선택 부분
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


# 맞서 싸우는 부분
def fight():
    bear_stat = int(100)
    att_num = int(1)

    print("당신은 2번을 선택하셨습니다.")
    print("당신은 6번의 공격 안에 곰을 물리쳐야 합니다.")
    print("곰의 초기 체력은 100입니다.\n")

    while att_num <= 6:
        ra = random.randrange(1, 31)
        bear_stat -= ra

        if bear_stat + ra > 0:
            print(str(att_num) + "번째 공격으로 곰의 체력이 " + str(ra) + "만큼 떨어졌습니다.")
            print("남아 있는 곰의 체력은 " + str(bear_stat) + "입니다.\n")
            time.sleep(1)
        else:
            break
        att_num += 1

    if bear_stat >= 0:
        print("당신이 졌군요. ㅠㅠ")
    elif bear_stat < 0:
        print("승리! 곰 가죽을 얻었습니다.!!")


# 메인 함수
while human_num <= 10:
    print("나무를 " + str(human_num) + "번 찍었습니다.")
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
    human_num += 1


'''
제출 과제 내용 : 
        주석처리
        



'''