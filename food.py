for i in range(1, 4):
	print("밥묵으러 가자 메뉴를 선택하세요")
	print("치킨 피자 햄버거")
	a = str(input(str(i) + " 선택:"))
	print("%s를 선택하셨습니다" % a)
	if (a == '치킨'):
		print("맛잇다\n")
	elif (a == '피자'):
		print("맛있다!!\n")
	elif (a == '햄버거'):
		print("맛앗다\n")
	else:
		print("잘못 선택하셧습니다")