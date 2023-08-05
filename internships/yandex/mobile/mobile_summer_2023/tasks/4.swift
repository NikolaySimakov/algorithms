var k = Int(readLine()!)!
var n = Int(readLine()!)!
let input = readLine() ?? ""
let arr = input.split(separator: " ").compactMap { Int($0)! }

var minCount = Int.max

func pow_(_ a: Int, _ b: Int) -> Int {
    var result = 1
    for _ in 0..<b {
        result *= a
    }
    return result
}

for i in 0..<n {
    if arr[i] == 0 {
        minCount = 0
        break
    }

    let count = pow_(2, i)
    let div = k % count == 0 ? Int(Float(k) / Float(count)) : Int(Float(k) / Float(count)) + 1
    let sum_ = div * arr[i]
    
    if sum_ < minCount {
        minCount = sum_
    }
}

print(minCount)