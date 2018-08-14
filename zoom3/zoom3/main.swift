import Foundation
import Glibc

// you can write to stdout for debugging purposes, e.g.
// print("this is a debug message")

public func solution(_ S : inout String, _ T : inout String) -> String {
    if S == T {
        return "NOTHING"
    }
    
    if abs(S.characters.count - T.characters.count) >= 2 {
        return "IMPOSSIBLE"
    }
    
    var SArray = S.characters.map { String($0) }
    var TArray = T.characters.map { String($0) }
    
    //    print(diff(SArray, TArray))
    
    if S.characters.count == T.characters.count {
        var diffArray: [String] = []
        for index in 0..<SArray.count {
            if SArray[index] != TArray[index] {
                diffArray.append(SArray[index])
            }
        }
        
        if diffArray.count == 2 {
            return "SWAP \(diffArray[0]) \(diffArray[1])"
        } else {
            return "IMPOSSIBLE"
        }
    }
    
    if S.characters.count < T.characters.count {
        while true {
            if let first = SArray.first, let index = TArray.index(of: first) {
                var subArray = TArray[index..<TArray.count]
                while true {
                    if SArray.first == subArray.first && SArray.first != nil && subArray.first != nil {
                        TArray.remove(at: TArray.index(of: subArray.removeFirst())!)
                        SArray.removeFirst()
                    } else {
                        break
                    }
                }
            } else {
                break
            }
        }
        
        if SArray.isEmpty == true && TArray.count == 1 {
            return "INSERT \(TArray.first!)"
        } else {
            return "IMPOSSIBLE"
        }
    }
    
    if S.characters.count > T.characters.count {
        while true {
            if let first = TArray.first, let index = SArray.index(of: first) {
                var subArray = SArray[index..<SArray.count]
                while true {
                    if TArray.first == subArray.first && TArray.first != nil && subArray.first != nil {
                        SArray.remove(at: SArray.index(of: subArray.removeFirst())!)
                        TArray.removeFirst()
                    } else {
                        break
                    }
                }
            } else {
                break
            }
        }
        
        if TArray.isEmpty == true && SArray.count == 1 {
            return "REMOVE \(SArray.first!)"
        } else {
            return "IMPOSSIBLE"
        }
    }
    
    return "IMPOSSIBLE"
    
}
