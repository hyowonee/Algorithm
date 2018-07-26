pointNum = int(input())
count = [0] * 4
axisCount = 0

for i in range(0, pointNum):
  x, y = map(int, input().split(' '))
  if x > 0 and y > 0:
    count[0] += 1
  elif x > 0 and y < 0:
    count[3] += 1
  elif x < 0 and y > 0:
    count[1] += 1
  elif x < 0 and y < 0:
    count[2] += 1
  else:
    axisCount += 1

for i in range(0, 4):
  print("Q%d: %d" % (i + 1, count[i]))
print("AXIS: %d" % axisCount)