from datetime import datetime

class Client:
  logInTime = None
  logOutTime = None
  clientID = -1

clientList = [Client() for i in range(10)]
logNum, thatTime = input().split('|')
thatTime = datetime.strptime(thatTime, '%H:%M:%S')
for _ in range(0, int(logNum)):
    logTime, logType, taskID, clientID = input().split('|')
    clientID = int(clientID)
    clientList[clientID].clientID = clientID

    if logType == "I":
      clientList[clientID].logInTime = datetime.strptime(logTime, '%H:%M:%S')
    else:
      clientList[clientID].logOutTime = datetime.strptime(logTime, '%H:%M:%S')

for i in range(0, 10):
  if clientList[i].clientID == -1:
    print("%d %d" % (i, 0))
    continue
  if clientList[i].logInTime <= thatTime and thatTime < clientList[i].logOutTime:
    print("%d %d" % (i, 1))
  else:
    print("%d %d" % (i, 0))
    
# 6|00:01:00
# 00:00:50|I|abcde01|9
# 00:00:55|I|cbcde02|1
# 00:00:59|O|cbcde02|1
# 00:00:59|I|c1cce03|3
# 00:01:05|O|abcde01|9
# 00:01:09|O|c1cce03|3