for i in range(1, 4):
  print("밥묵으러 가자")
  print("치킨 피자 햄버거")
  a = str(input(str(i) + " 선택:"))
  print("%s를 선택하셨습니다" % a)
  if(a=='치킨') :
    print("맛잇다")
  elif(a=='피자') :
    print("맛있다!!")
  elif(a=='햄버거') :
    print("맛앗다")
  else :
    print("잘못 선택하셧습니다")
