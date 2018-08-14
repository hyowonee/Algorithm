// 11866
// 문제
// 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 M(≤ N)이 주어진다. 이제 순서대로 M번째 사람을 제거한다.
// 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
// 원에서 사람들이 제거되는 순서를 (N, M)-조세퍼스 순열이라고 한다. 예를 들어 (7, 3)-조세퍼스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
// N과 M이 주어지면 (N,M)-조세퍼스 순열을 구하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 N과 M이 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ M ≤ N ≤ 1,000)

// 출력
// 예제와 같이 조세퍼스 순열을 출력한다.

import Foundation

let getInput = readLine()!.split(separator: " ").map{Int($0)!}
let numberOfPeople: Int = getInput[0]
var criteria: Int = getInput[1]
var addNumber: Int = criteria
criteria -= 1
var peolpe: [Int] = []
var result: [Int] = []

for i in 0..<numberOfPeople {
    peolpe.append(i + 1)
}

while !peolpe.isEmpty {
    if criteria <= peolpe.count {
        result.append(peolpe[criteria])
        peolpe.remove(at: criteria)
    }
    else {
        result.append(peolpe[criteria - peolpe.count])
        peolpe.remove(at: peolpe[criteria - peolpe.count])
        criteria -= peolpe.count
        
    }
    
    print("지금 기준 : \(criteria)")
    criteria += addNumber

}
print("<\(result.map{Int($0)})>")


//'1 2 3 4 5 6 7 -> 3 3
//1 2 '4 5 6 7 -> 6 6
//1 2 4 5 '7  -> 2 9-7
//1 '4 5 7 -> 7
//'1 4 5 -> 5
//'1 4 1 -> 1
//4 -> 4



