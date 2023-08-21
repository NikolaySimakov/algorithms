function getPINs(observed) {
    if (observed.length === 0) {
        return ['']
    }

    const num = +observed.charAt(0)

    const options = {
        1: [2, 4],
        2: [1, 3, 5],
        3: [2, 6],
        4: [1, 5, 7],
        5: [2, 4, 6, 8],
        6: [3, 5, 9],
        7: [4, 8],
        8: [5, 7, 9, 0],
        9: [6, 8],
        0: [8],
    }

    let res = []

    for (let n of [num, ...options[num]]) {
        for (let op of getPINs(observed.slice(1))) {
            res.push(n.toString() + op)
        }
    }

    return res
}