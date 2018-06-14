virus = {}
computerNum = int(input())
infected = [False] * (computerNum + 1)
connectionNum = int(input())

def check(checkList):
  for num in checkList:
    infected[num] = True
    if num in virus:
      check(virus[num])

for _ in range(connectionNum):
  computer = list(map(int, input().split(' ')))
  computer.sort()
  if computer[0] not in virus:
      virus[computer[0]] = []
  virus[computer[0]].append(computer[1])
check(virus[1])

print(infected.count(True))