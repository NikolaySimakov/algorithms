
// Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n, упорядоченные лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).

// В задаче используются только круглые скобки.

// Желательно получить решение, которое работает за время, пропорциональное общему количеству правильных скобочных последовательностей в ответе, и при этом использует объём памяти, пропорциональный n.

function generateParenthesis(n) {
    const res = []
    const stack = []

    const backtracking = (open = 0, close = 0) => {
        if (open === n && close === n) {
            res.push(stack.join(''))
            return
        }
        if (open < n) {
            stack.push('(')
            backtracking(open+1, close)
            stack.pop()
        }
        if (close < open) {
            stack.push(')')
            backtracking(open, close+1)
            stack.pop()
        }
    }

    backtracking()
    return res
}

const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin
})

let n = 0

rl.on('line', (line) => {
    n = +line
}).on('close', () => {
    const ans = generateParenthesis(n)
    for (let a of ans) {
        process.stdout.write(a + '\n')
    }
})