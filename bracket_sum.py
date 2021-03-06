# 2504
# 문제
## 4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.
## 1. 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다. 
## 2. 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다. 
## 3. X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
## 예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다. 
## 우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다. 
## 1. ‘()’ 인 괄호열의 값은 2이다.
## 2. ‘[]’ 인 괄호열의 값은 3이다.
## 3. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
## 4. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
## 5. 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.

# 입력
## 첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.

# 출력
## 첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다. 

def isRightBracket(brackets):
  checkOpen1 = False
  checkClose1 = False
  checkOpen2 = False
  checkClose2 = False
  for bracket in brackets:
    if bracket  == '(:
      checkOpen1 = True
    if bracket == '[':
      checkOpen2 = True
  if check != 0:
    return False
  return True

if isRightBracket(input()):
  print(True)