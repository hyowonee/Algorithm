def exeCuteCommand(string):
  string = string.split(' ')
  if string[0] == "push_back":
    deque.append(int(string[1]))
  elif string[0] == "push_front":
    deque.insert(0, int(string[1]))
  elif string[0] == "pop_front":
    if not deque:
      print(-1)
    else:
      print(deque.pop(0))
  elif string[0] == "pop_back":
    if not deque:
      print(-1)
    else:
      print(deque.pop())
  elif string[0] == "size":
    print(len(deque))
  elif string[0] == "empty":
    if not deque:
      print(1)
    else:
      print(0)
  elif string[0] == "front":
    if not deque:
      print(-1)
    else:
      print(deque[0])
  elif string[0] == "back":
    if not deque:
      print(-1)
    else:
      print(deque[-1])

numOfCommand = int(input())
deque = []
for _ in range(numOfCommand):
  exeCuteCommand(input())