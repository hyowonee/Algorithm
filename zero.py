import math

def zeroNum(num):
  two = 0
  five = 0
  for i in range(1, int(math.sqrt(num + 1))):
    number = i
    while(number % 5 == 0):
      five += 1
      number /= 5    
  # print("two : %d" % two)
  # print("five : %d" % five)1470*
  return five * 2
      
nums = int(input())
for _ in range(0, nums):3
  num = int(input())
  print(zeroNum(num))
print(1470*1470)