def isHansu(num):
  isSame = True
  number = str(num)
  if len(number) <= 1:
    return True
  diff = int(number[1]) - int(number[0])
  for i in range(len(number) - 1):
    if diff != (int(number[i+1]) - int(number[i])):
      isSame = False
  return isSame

getNum = int(input())
count = 0
for j in range(1, getNum + 1):
  if isHansu(j):
    count += 1
print(count)