# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
vowels = ['a', 'e', 'i', 'o', 'u']

def checkPassword1(inputWord):
    if any(x in inputWord for x in vowels):
      checkPassword2()
    else:
      failedPassword()

def checkPassword2():
  vowelCount = 0
  consonantCount = 0
  for letter in inputWord:
    if letter in vowels:
      vowelCount += 1
      consonantCount = 0
    else:
      vowelCount = 0
      consonantCount += 1
    if (vowelCount >= 3 or consonantCount >= 3):
      failedPassword()
      return
  # print("passed check2, current Word is %s" % inputWord)
  checkPassword3()

def checkPassword3():
  sameLetter = ""
  for letter in inputWord:
    if sameLetter == letter:
      if letter == 'e' or letter == 'o':
        continue
      else:
        failedPassword()
        return
    else:
      sameLetter = letter
  # print("passed check3, current Word is %s" % inputWord)
  print("<" + inputWord + ">" + " is acceptable.")

def failedPassword():
  print("<" + inputWord + ">" + " is not acceptable.")

inputWords = []
while True:
  inputString = input()
  if inputString == '' or inputString == "end":
    break
  else:
    inputWords.append(inputString)

for inputWord in inputWords:
  checkPassword1(inputWord)

#!/usr/bin/env python

# class PasswordValidator:
#   vowels = ['a', 'e', 'i', 'o', 'u']

#   def validate(self, inputWord):
#     check = True
#     check = check & self.vowelValidate(inputWord)
#     check = check & self.continuousVowelValidate(inputWord)
#     check = check & self.twiceCheckValidate(inputWord)

#     if check == True:
#       print('<' + inputWord + '>' + ' is acceptable.')
#     else:
#       print('<' + inputWord + '>' + ' is not acceptable.')
  
#   def vowelValidate(self, inputWord):
#     return any(x in inputWord for x in self.vowels)

#   def continuousVowelValidate(self, inputWord):
#     vowelCount = 0
#     consonantCount = 0
#     for letter in inputWord:
#       if letter in self.vowels:
#         vowelCount += 1
#         consonantCount = 0
#       else:
#         vowelCount = 0
#         consonantCount += 1
#       if (vowelCount >= 3 or consonantCount >= 3):
#         return False
#     return True

#   def twiceCheckValidate(self, inputWord):
#     sameLetter = ''
#     for letter in inputWord:
#       if sameLetter == letter:
#         if letter == 'e' or letter == 'o':
#           continue
#         return False
#       sameLetter = letter
#     return True

# inputWords = []
# while True:
#   inputString = raw_input()
#   if inputString == 'end':
#     break
    
#   inputWords.append(inputString)

# validator = PasswordValidator()
# for inputWord in inputWords:
#   validator.validate(inputWord)