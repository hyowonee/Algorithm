def isDivisable(numberOfSugar):
  tmpFive = 10000
  tmpThree = 10000
  if (numberOfSugar % 5 == 0):
    tmpFive = int(numberOfSugar / 5)
  if (numberOfSugar % 3 == 0):
    tmpThree = int(numberOfSugar / 3)
  else :
    return -1
  return (min(tmpThree, tmpFive))

def isIndivisable(numberOfSugar):
  return (max(firstCase(numberOfSugar), secondCase(numberOfSugar)))

def firstCase(numberOfSugar):
  fiveSugar = int(numberOfSugar / 5)
  numberOfSugar %= 5
  threeSugar = int(numberOfSugar / 3)
  numberOfSugar %= 3
  if(numberOfSugar != 0):
    return (-1)
  else:
    return (fiveSugar + threeSugar)

def secondCase(numberOfSugar):
  threeSugar = int(numberOfSugar / 3)
  numberOfSugar %= 3
  fiveSugar = int(numberOfSugar / 5)
  numberOfSugar %= 5
  if(numberOfSugar != 0):
    return (-1)
  else:
    return (fiveSugar + threeSugar)

numberOfSugar = int(input())
if isIndivisable(numberOfSugar) == -1:
  print("여기다리")
  print(isDivisable(numberOfSugar))
else:
  print(min(isDivisable(numberOfSugar), isIndivisable(numberOfSugar)))