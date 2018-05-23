from collections import Counter

input_num = int(input())
nums = input().split(' ')
counter = Counter(nums)
for key, value in counter.items():
  if value == 1:
    print(key)