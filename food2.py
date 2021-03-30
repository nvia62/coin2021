### 아래 전체를 반복 ###
import random
for i in range(1, 4):
    print("밥무러 가자")
    print("메뉴는? ")
    menu1 = '학식', '분식', '중식'
    print("1.학식 2.분식 3.중식. 4랜덤") 
    menu = input(str(i) + ".입력: ")
    #만약에 사용자가 입력값이 1 과 같으면
    if menu == '1':
        print("학식 먹어라\n")
    if menu == '2':
        print("분식 먹어라\n")
    if menu == '3':
        print("중식 먹어라\n")
    if menu == '4':
        print("내맘대로")
        print(random.choice(menu1))
        print("")
    ### 여기까지 반복 ###