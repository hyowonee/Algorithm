import math

n = int(input())
length = pow(3, n)
result = []

def making(array, length):
  before = ['-'] * int(length / 3)
  present = ['-'] * int(length / 3)
  after = ['-'] * int(length / 3)

  if len(array) < 2:
    return array
  else:
    for string in present:
      string = ''
    array = making(before) + present + making(after)
    length /= 3
    return array
  

print(making(result, length))

# str1 = ''.join(list1)