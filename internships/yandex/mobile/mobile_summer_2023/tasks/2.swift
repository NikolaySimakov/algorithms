var n = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").map { Int($0)! }

var res = ""
var temp: Set<Int> = []

for i in 0..<n {
    temp.insert(arr[i])
    
    if temp.contains(n) {
        var add = ""
        
        while let index = temp.firstIndex(of: n) {
            add += "\(temp[index]) "
            temp.remove(n)
            n -= 1
        }
        res += "\(add)\n"
    } else {
        res += "\n"
    }
}

if !temp.isEmpty {
    res += "\(temp.map { String($0) }.joined(separator: " "))\n"
}

print(res)