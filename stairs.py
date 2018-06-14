def sumScore(beforeScore, index):
  currentScore = beforeScore

  return currentScore
    
numStairs = int(input())
stairs = []
for _ in range(0, numStairs):
  stairs.append(int(input()))

startScore = stairs[0]

for i in range(0, numStairs - 1):
  sumScore(startScore, i)