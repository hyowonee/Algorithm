//
//  main.swift
//  zoom4
//
//  Created by Hyowon Choi on 2018. 8. 4..
//  Copyright © 2018년 Hyowonee. All rights reserved.
//

import Foundation

func solution(S: Tree) -> Int {
    var stack: [Tree] = []
    var max = 0
    stack.append(S)
    
    while stack.isEmpty == false {
        let t = stack.removeFirst()
        if t.l != nil {
            stack.append(t.l!)
        }
        if t.r != nil {
            stack.append(t.r!)
        }
        let depth = balancedDepth(t: t, depth: 1)
        let size = Int(pow(Double(2), Double(depth))) - 1
        if size > max {
            max = size
        }
    }
    
    return max
}

func balancedDepth(t: Tree?, depth: Int) -> Int {
    if t?.l != nil && t?.r != nil {
        return min(balancedDepth(t: t?.l, depth: depth + 1), balancedDepth(t: t?.r, depth: depth + 1))
    }
    return depth
}
