/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const stack = []
    let count = 0

    const d = new Map()
    d.set('I', 1)
    d.set('V', 5)
    d.set('X', 10)
    d.set('L', 50)
    d.set('C', 100)
    d.set('D', 500)
    d.set('M', 1000)

    for (let i = 0; i < s.length; i++) {
        const cur = d.get(s[i])
        const next = d.get(s[i+1])

        if (cur <  next) {
            count += next - cur
            i++
        } else {
            count += cur
        }
    }

    return count

};