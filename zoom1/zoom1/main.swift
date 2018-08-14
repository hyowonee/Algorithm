import Foundation
import Glibc

class Time {
    var hour: Int = 0 {
        didSet {
            if hour >= 24 {
                hour = 0
            }
        }
    }
    var minute: Int = 0 {
        didSet {
            if minute >= 60 {
                hour += 1
                minute = 0
            }
        }
    }
    var second: Int = 0 {
        didSet {
            if second >= 60 {
                minute += 1
                second = 0
            }
        }
    }
    
    let formatter = DateFormatter()
    
    init(string: String) {
        let digits = string._split(separator: ":").map { Int($0)! }
        hour = digits[0]
        minute = digits[1]
        second = digits[2]
        
        formatter.dateFormat = "H:m:s"
    }
    
    func toDate() -> Date {
        return formatter.date(from: "\(hour):\(minute):\(second)")!
    }
    
    func toDigitsString() -> String {
        return "\(hour < 10 ? "0\(hour)" : "\(hour)")\(minute < 10 ? "0\(minute)" : "\(minute)")\(second < 10 ? "0\(second)" : "\(second)")"
    }
}

public func solution(_ S : inout String, _ T : inout String) -> Int {
    let time1 = Time(string: S)
    let time2 = Time(string: T)
    var interestingCount = 0
    while time1.toDate() <= time2.toDate() {
        let distinctCount = Array(Set(time1.toDigitsString().characters.map { String($0) })).count
        if distinctCount <= 2 {
            interestingCount += 1
        }
        time1.second += 1
    }
    return interestingCount
}
