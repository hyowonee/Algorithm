stringNum = int(input())
strings = []
result = []

for i in range(0, stringNum):
  strings.append(input())
  
stringLen = len(strings[0])
letters = strings[0]

for j in range(0, stringLen):
  isLetterSame = True
  currentLetter = ""
  for i in range(0, stringNum):
    currentLetter = strings[i][j]
    if currentLetter != letters[j]:
      isLetterSame = False
       
  if isLetterSame:
    result.append(currentLetter)
  else:
    result.append("?")

print(''.join(map(str, result)))
