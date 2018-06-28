# def sumScore(beforeScore, index):
#   currentScore = beforeScore

#   return currentScore
    
# numStairs = int(input())
# stairs = []
# for _ in range(0, numStairs):
#   stairs.append(int(input()))

# startScore = stairs[0]

# for i in range(0, numStairs - 1):
#   sumScore(startScore, i)



# -*- coding: utf-8 -*-
n = int(input()) # n 입력
items = []
matrix = [[0]*2 for i in range(n)] # n*2 크기의 2차원 배열 생성
# 현재 계단의 상태는 두 가지 있을 수 있다
# 1. 이전 계단에서 한 칸 올라왔을 떄
# 2. 이전 계단에서 두 칸 올라왔을 때
# 그렇기 때문에 두 가지 상태를 저장할 수 있도록 2차원 배열이 필요하다

for _ in range(0, n):
  items.append(int(input())) # 계단 점수 입력

for i in range(0, n):
  if matrix[i-2][0] > matrix[i-2][1]: # 두 칸 올라갈때 첫 번째 상태가 두 번째 상태보다 클 경우
    matrix[i][0] = matrix[i-2][0] + items[i] # 첫 번째 상태를 저장
  else:
    matrix[i][0] = matrix[i-2][1] + items[i] # 아니면 두 번째 상태를 저장
  matrix[i][1] = matrix[i-1][0] + items[i] # 한 칸 올라가는 경우는 무조건 두 번째 상태에 저장

if matrix[n-1][0] > matrix[n-1][1]:
  print(matrix[n-1][0]) # 결과적으로 마지막 계단에 올라왔을 때 첫 번쨰 상태가 크면 첫 번째 상태를 저장
else:
  print(matrix[n-1][1]) #  아니라면 두 번째 상태를 저장