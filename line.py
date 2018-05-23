from collections import Counter
import operator

manNum, compareNum = map(int, input().split())
nums = list()
result = str()
for _ in range(0, compareNum):
  inputNums = input().split(' ')
  for num in inputNums:
    nums.append(num)
counter = Counter(nums)
sortedNum = sorted(counter.items(), key = operator.itemgetter(1), reverse = False)

for i in range(0, manNum):
  result += sortedNum[i][0]
  if i == manNum - 1:
    break
  else:
    result += ' '
print(result)