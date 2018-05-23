def solution(n):
    numString = str(n)
    sum = 0
    for num in numString:
      sum += int(num)
    if (sum > 9):
      return solution(sum)
    else:
      return (sum)  

      
solution(456789)