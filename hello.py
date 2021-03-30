import random
rand = '맞아죽었다', '살았다','퉁퉁이가 기겁하면서 도망쳤다'
print("도라에몽이 길을 가다 퉁퉁이를 만났다 어떻게할것인가?")
print("1. 맞서싸운다")
print("2. 도망간다")
print("3. 아무것도 안한다")
print("4. 미친척한다")
a = int(input("선택: "))
print("%d번을 입력하셧습니다" % a)
if (a==1):
    print("맞아죽었다")
elif (a==2):
    print("무사히 도망쳣다")
elif (a==3):
    print("맞아죽었다")
elif (a==4):
    print(random.choice(rand))
else:
    print("잘못된 선택지 입니다")

