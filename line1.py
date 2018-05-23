import math

playNum = int(input())
for _ in range(0, playNum):
    BrownScore = []
    ConyScore = []
    Brown = 0
    Cony = 0
    stoneNum = int(input())
    for i in range(0, stoneNum):
        x, y, team = input().split(' ')
        x = int(x)
        y = int(y)
        if team == "Brown":
            BrownScore.append(pow(x,2)+pow(y,2))
        else:
            ConyScore.append(pow(x,2)+pow(y,2))

    if min(BrownScore) < min(ConyScore):
      winnerTeam = "Brown"
      winnerScore = min(BrownScore)
      for score in BrownScore:
        if score < min(ConyScore):
          Brown += 1
      print("%s %d" % (winnerTeam, Brown))
    else:
      winnerTeam = "Cony"
      winnerScore = min(ConyScore)
      for score in ConyScore:
        if score < min(BrownScore):
          Cony += 1
      print("%s %d" % (winnerTeam, Cony))
    
    # print(BrownScore)
    # print(ConyScore)
    # print(winnerTeam)
    # print(winnerScore)
    # print(BrownScore)
    