# 1932
# 문제
## 위 그림은 크기가 5인 정수 삼각형의 한 모습이다.
## 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
## 삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

# 입력
# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

# 출력
## 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

n = int(input())
array = []
for i in range(n):
  array.append(list(map(int, input().split(' '))))

for i in range(1, n): # 맨 위는 계산 안해도 되기 때문에 0이 아닌 1부터 시작
  for j in range(0, len(array[i])):
    if j == 0: # 가장 왼쪽은 경우의 수가 하나기 때문에 무조건 더해줘도 상관 없음
      array[i][0] = array[i-1][j] + array[i][j]
    elif j == len(array[i])-1: # 마찬가지로 가장 오른쪽도 경우의 수가 하나
      array[i][j] = array[i-1][j-1] + array[i][j]
    else:
      # 중간에 있는 숫자의 경우 왼쪽 위와 바로 위쪽의 값 중 더 큰 값으로 대체
      array[i][j] = max(array[i-1][j] + array[i][j], array[i-1][j-1] + array[i][j])

print(max(array[n-1])) # 마지막 리스트 중 가장 큰 값을 출력
