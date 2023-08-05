let input = readLine() ?? ""
let numbers = input.split(separator: " ").compactMap { Int($0) }
let n = numbers[0]
let m = numbers[1]

var blueLamps = [[Int]]()
var redLamps = [[Int]]()
var yellowLamps = [[Int]]()
var colors = [[String]]()

for _ in 0..<n {
    let line = readLine() ?? ""
    let lamps = line.compactMap { Int(String($0)) }
    blueLamps.append(lamps)
}

for _ in 0..<n {
    let line = readLine() ?? ""
    let lamps = line.compactMap { Int(String($0)) }
    redLamps.append(lamps)
}

for _ in 0..<n {
    let line = readLine() ?? ""
    let lamps = line.compactMap { Int(String($0)) }
    yellowLamps.append(lamps)
}

for _ in 0..<n {
    let line = readLine() ?? ""
    let colorsRow = line.map { String($0) }
    colors.append(colorsRow)
}

func canDisplayAdvertisement() -> Bool {
    for i in 0..<n {
        for j in 0..<m {
            if colors[i][j] != "D" {
                if colors[i][j] == "B" && blueLamps[i][j] == 0 {
                    return false
                }
                if colors[i][j] == "R" && redLamps[i][j] == 0 {
                    return false
                }
                if colors[i][j] == "Y" && yellowLamps[i][j] == 0 {
                    return false
                }
                if colors[i][j] == "P" && (blueLamps[i][j] == 0  redLamps[i][j] == 0) {
                    return false
                }
                if colors[i][j] == "G" && (blueLamps[i][j] == 0  yellowLamps[i][j] == 0) {
                    return false
                }
                if colors[i][j] == "O" && (redLamps[i][j] == 0  yellowLamps[i][j] == 0) {
                    return false
                }
                if colors[i][j] == "V" && (blueLamps[i][j] == 0  redLamps[i][j] == 0 || yellowLamps[i][j] == 0) {
                    return false
                }
            }
        }
    }
    return true
}

if canDisplayAdvertisement() {
    print("YES")
} else {
    print("NO")
}