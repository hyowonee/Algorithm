def isDivisableByOnlyThree(num):
  return int(num / 3)

def isDivisableByOnlyFive(num):
  return int(num / 5)

def isDivisableByEight(num):
  return int(num / 8 * 2)

def isNotDivisable(num):
  tmpNum1 = num
  tmpNum2 = num

  threeNum1 = tmpNum1 / 3
  tmpNum1 %= 3
  fiveNum1 = tmpNum1 / 5
  tmpNum1 %= 5
  print("tmpNum1: %d, threeNum1 : %d, fiveNum1 : %d" % (tmpNum1, threeNum1, fiveNum1))

  threeNum2 = tmpNum2 / 5
  tmpNum2 %= 5
  fiveNum2 = tmpNum2 / 3
  tmpNum2 %= 3
  print("tmpNum2: %d, threeNum2 : %d, fiveNum2 : %d" % (tmpNum2, threeNum2, fiveNum2))

  if tmpNum1 == 0 and tmpNum2 == 0:
    print("둘 다 나누어 떨어지는 경우")
    return min(fiveNum1 + threeNum1, fiveNum2 + threeNum2)
  elif tmpNum1 == 0 and tmpNum2 != 0:
    print("3으로 먼저 나누면 나누어 떨어지는 경우")
    return fiveNum1 + threeNum1
  elif tmpNum1 != 0 and tmpNum2 == 0:
    print("5로 먼저 나누면 나누어 떨어지는 경우")
    return fiveNum2 + threeNum2
  else:
    print("둘다 안나누어지는 경우")
    return -1

num = int(input())
if num % 3 == 0 and num % 5 != 0:
  print("3임")
  print(isDivisableByOnlyThree(num))
elif num % 3 != 0 and num % 5 == 0:
  print("5임")
  print(isDivisableByOnlyFive(num))
elif num % 3 == 0 and num % 5 == 0:
  print("8임")
  print(isDivisableByEight(num))
  
else:
  print("다른경우")
  print(isNotDivisable(num))