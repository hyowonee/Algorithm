# 1913
# 문제
## 홀수인 자연수 N(3≤N≤999)이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N*N의 표에 늘어놓을 수 있다.
## N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오. 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오. 예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.

# 입력
## 첫째 줄에 홀수인 자연수 N이 주어진다. 둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.

# 출력
## N개의 줄에 걸쳐 표를 출력한다. 각 줄에 N개의 자연수를 한 칸씩 띄어서 출력하면 되며, 자릿수를 맞출 필요가 없다. 
## N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력한다.

n = int(input())
num = int(input())
array = [[0] * n for i in range(n)]

## swift
# let n = Int(readLine():!)!
# let m = Int(readLine()!)!
# var array = Array(repeating: Array(repeating: 0, count: n), count: n)

# var direction = 0 // 0 down, 1 right, 2 up, 3 left
# var directionArray = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# var count = n * n
# var x = 0, y = 0
# var saveX = 0, saveY = 0
# while count >= 1 {
#   array[y][x] = count
  
#   if count == m {
#     saveY = y
#     saveX = x
#   }
  
#   let dy = directionArray[direction][0]
#   let dx = directionArray[direction][1]
#   if n <= y + dy || 0 > y + dy ||
#     n <= x + dx || 0 > x + dx ||
#     array[y + dy][x + dx] != 0 {
#     direction = (direction + 1) % 4
#   }
  
#   y += directionArray[direction][0]
#   x += directionArray[direction][1]
#   count -= 1
# }