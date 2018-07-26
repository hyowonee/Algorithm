while True:
    num = int(input())
    if num == 0:
      break
    elif num < 10:
      print(num)
    else:
      numStr = str(num)
      result = list()
      result.append(num)
      while True:
        multi = 1
        for number in numStr:
            multi *= int(number)
        numStr = str(multi)
        result.append(multi)
        if multi < 10:
          break
      result = ' '.join(str(e) for e in result).strip()
      print(result)