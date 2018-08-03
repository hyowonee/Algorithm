# 1924
# 문제
## 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

# 입력
## 첫째 줄에 빈 칸을 사이에 두고 x(1≤x≤12)와 y(1≤y≤31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

# 출력
## 첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

getMonth, getDay = map(int, input().split(' '))
calendar = {31: [1, 3, 5, 7, 8, 10, 12], 
            30: [4, 6, 9, 11],
            28: [2]}

date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day = getDay

for i in range(1, getMonth):
  for days, month in calendar.items():
    if i in month:
      day += days

print(date[day % 7])


