import sys

def qsort(array):
  less = []
  equal = []
  greater = []
  if len(array) > 1:
    pivot = array[0]
    for x in array:
      if x < pivot:
          less.append(x)
      if x == pivot:
          equal.append(x)
      if x > pivot:
          greater.append(x)
    return qsort(less) + equal + qsort(greater)
  else:  
    return array

number, whereNum = map(int, sys.stdin.readline().split(' '))

numList = list(map(int, sys.stdin.readline().split(' ')))
numList = qsort(numList)
print(numList[whereNum - 1])

