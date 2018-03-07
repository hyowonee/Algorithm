# 싱근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.
# 두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 이 때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최소값과 최대값을 구해 출력하는 프로그램을 작성하시오.

firstNum, secondNum = input().split()
maxNum = ""
minNum = ""

def isMax(numberString):
  for index, number in enumerate(numberString):
    if(number == "5"):
      numberString = numberString.replace(numberString[index], "6")
  maxNum = int(numberString)
  return maxNum
      
def isMin(numberString):
  for index, number in enumerate(numberString):
    if(number == "6"):
      numberString = numberString.replace(numberString[index], "5")
  minNum = int(numberString)
  return minNum

maxResult = isMax(firstNum) + isMax(secondNum)
minResult = isMin(firstNum) + isMin(secondNum)
print("%d %d" % (minResult, maxResult))