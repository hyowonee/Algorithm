# 입력은 한 줄로 이루어져 있고, 최대 100글자의 영어 알파벳 대문자, 소문자, 그리고 하이픈 ('-', 아스키코드 45)로만 이루어져 있다. 
# 첫번째 글자는 항상 대문자이다. 그리고, 하이픈 뒤에는 반드시 대문자이다. 그 외의 모든 문자는 모두 소문자이다.

inputStr = input().split('-')
resultStr = str()
for string in inputStr:
  resultStr += string[0]
print(resultStr)