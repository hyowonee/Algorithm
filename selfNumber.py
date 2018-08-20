array = [True] * 10001

def checkSeflNum(number):
  numberString = str(number)
  sumNum = 0
  for num in numberString:
    sumNum += int(num)
  if (number + sumNum) > 10000:
    return
  array[number + sumNum] = False
  if (number + sumNum) <= 10000:
    checkSeflNum(number + sumNum)
    
for i in range(1, 10001):
  checkSeflNum(i)
      
for i in range(1, 10001):
  if array[i]:
    print(i)