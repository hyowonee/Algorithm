numberOfTuple = int(input())
pointList = list()
sortList = list()

for _ in range(0, numberOfTuple):
  points = []
  points = input().split()
  pointList.append(points)

sortList = sorted(pointList, key = lambda point: point[1],)
# for i in range(0, len(sortList) - 1):
#   if point[i][1] == pointList[i+1][1]:

for point in sortList:
  print(point)

  
# print(tupleList)
# print(tupleList[0])
# print(tupleList[0][0])