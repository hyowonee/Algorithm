// 11725
// 문제
// 루트 없는 트리가 주어진다. 이 때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

// 출력
// 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

import Foundation

//class Node {
//    var value: Int
//    var children: [Node] = []
//    weak var parent: Node? // cycle 유지를 피하기 위한 weak
//    var next: Node?
//    weak var previous: Node?
//
//    init(value: Int) {
//        self.value = value
//    }
//
//    func add(child: Node) {
//        children.append(child)
//        child.parent = self
//    }
//}
//
//var numberOfNodes: Int = Int(readLine()!)!
//let parentNode = Node(value: 1)
//var nodeList: [Node]?
//
//for _ in 0..<(numberOfNodes - 1) {
//    var input = readLine()!.split(separator: " ").map{Int($0)!}
//}


class Node {
    let value: Int
    var parent: Node?
    var children: [Node] = []
    
    init(value: Int) {
        self.value = value
    }
}

let n = Int(readLine()!)!

var nodes: [Node] = []

for index in 0..<n {
    nodes.append(Node(value: index + 1))
}

for _ in 0..<n-1 {
    let inputs = readLine()!.split(separator: " ").map { Int($0)! }
    let aInput = inputs[0] - 1
    let bInput = inputs[1] - 1
    nodes[aInput].children.append(nodes[bInput])
    nodes[bInput].children.append(nodes[aInput])
}

func setParent(_ node: Node) {
    node.children.forEach {
        if $0.parent == nil {
            $0.parent = node
            setParent($0)
        }
    }
}

setParent(nodes[0])

for index in 1..<n {
    print(nodes[index].parent!.value)
}
