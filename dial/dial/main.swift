// 5622
// 문제
// 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다.
// 다른 숫자를 누르려면 다이얼이 원래 위치로 돌아가기를 기다려야 한다.
// 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
// 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다.
// 예를 들어, UNUCIC는 868242와 같다. 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 시간을 구하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어는 2글자~15글자로 이루어져 있다.

// 출력
// 첫째 줄에 다이얼을 걸기 위해서 필요한 시간을 출력한다.
import Foundation

var time: Int = 0
var rule: [Int : [String]] = [2:["A", "B", "C"], 3:["D", "E", "F"], 4:["G" ,"H", "I"], 5:["J", "K", "L"],
                              6:["M", "N", "O"], 7:["P", "Q", "R", "S"], 8:["T", "U", "V"], 9:["W", "X", "Y", "Z"]]
let word: String = readLine()!
let alphaTime: Int = word.count

for letters in word {
    let letter: String = String(letters)
    for value in rule.values {
        let valueIndex = rule.values.index(of: value)
        if value.contains(letter) {
            time += rule.keys[valueIndex!]
            break
        }
    }
}

print(time + alphaTime)
