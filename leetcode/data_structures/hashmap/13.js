/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let count = 0

    const d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    for (let i = 0; i < s.length; i++) {
        const cur = d[s[i]]
        const next = d[s[i+1]]

        if (cur <  next) {
            count += next - cur
            i++
        } else {
            count += cur
        }
    }

    return count

};


/**
 * @param {string} s
 * @return {number}
 */
var romanToIntUsingStack = function(s) {
    const stack = []
    let count = 0

    const d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    for (let i = 0; i < s.length; i++) {
        const cur = d[s[i]]

        while (cur > d[stack[stack.length - 1]]) {
            let el = stack.pop()
            count -= d[el] * 2
        }

        stack.push(s[i])
        count += d[s[i]]
    }

    return count

};