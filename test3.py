def solution(string):
    getString = str(string)
    numString = str()
    resultNum = int()
     
    for getStr in getString:
      if "0" <= getStr and getStr <= "9":
        numString += getStr
      else:
        numString += ":"
    resultString = numString.split(":")
    for getStr in resultString:
      if getStr != "":
        if int(getStr) % 2 == 1:
          resultNum += int(getStr) * int(getStr)
    print(resultString)
    print(resultNum)

solution("ab2v9bc13j5jf4jv")