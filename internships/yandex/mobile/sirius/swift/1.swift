var arr = [String]()
var n: Int = 0
var sequence: String = ""

if let input = readLine() {
    if let count = Int(input) {
        n = count
    }
}

func findMax( _ str: String) -> Int {
    var res = 1
    var t_arr = [String]()
    
    let first = str.first ?? Character("")
    str.split(separator: first).forEach{ t_arr.append(String(String(first) + String($0)))}
    if let last = str.last, last == first, str.count > 1 {
        t_arr.append(String(first))
    }

    var max = 0
    t_arr.forEach{
        if $0.count > max { max = $0.count }
        if max > res { res = max }
    }
    return res
}

func find() -> Int {
    var res = 1
    var max = 1

    guard let inputSequence = readLine() else  { return res }
    sequence = inputSequence

    sequence.split(separator: "#").forEach {
        arr.append(String($0))
    }
    guard !arr.isEmpty else { return res }
    arr.forEach {
        max = findMax($0)
        if max > res { res = max }
    }

    return res
}

print(find())