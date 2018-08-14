// 1463
// 문제
// 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
// 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
// 2. X가 2로 나누어 떨어지면, 2로 나눈다.
// 3. 1을 뺀다.
// 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

// 입력
// 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.

// 출력
// 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다
import Foundation

var inputNum: Int = readLine().map{Int($0)}!!
var numArray: [Int] = Array(repeating: 0, count: inputNum + 1)
numArray[0] = 0
numArray[1] = 0

func makeOne(_ num: Int) -> Int {
    var minCount: Int = 0
    var index: Int = 1
    var number = num
    while true {
        if number % 3 == 0 && number > 1 {
            number /= 3
            minCount += 1
        }
        if number % 2 == 0 && number > 1{
            number /= 2
            minCount += 1
        }
        if  number > 1 {
            number -= 1
            minCount += 1
        }
        if number == 1 {
            numArray[index] = minCount
            break
        }
        index += 1
    }
    numArray[index] = min(numArray[index - 2], numArray[index - 1], numArray[index])
    
    return numArray[index]
}

print(makeOne(inputNum))




