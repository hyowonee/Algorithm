from collections import defaultdict

testCase = int(input())
for _ in range(testCase):
  result = 0
  multi = 1
  wear = defaultdict(list)
  wearCase = int(input())
  for i in range(wearCase):
    clothes, kind = input().split(' ')
    wear[kind].append(clothes)
  for key, value in wear.items():
    wear = dict(wear)
    result += len(wear[key])
    multi *= len(wear[key])
  if len(wear.keys()) > 1:
    print(result + multi)
  else:
    print(result)