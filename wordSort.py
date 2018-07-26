wordNum = int(input())
wordList = list()
for i in range(wordNum):
  word = input()
  if word not in wordList:
    wordList.append(word)
wordList.sort()
wordList.sort(key = len, reverse = False)

for word in wordList:
  print(word)