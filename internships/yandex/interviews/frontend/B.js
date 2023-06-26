// Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.

// Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.

const readline = require('readline');
 
const rl = readline.createInterface({
    input: process.stdin
});

let lines = [];
rl.on('line', (line) => {
    lines.push(+line);
}).on('close', () => {
    const [n, ...nums] = lines
    let result = 0;
    let count = 0

    for (let num of nums) {
        if (num === 1) {
            count++
        } else {
            result = Math.max(result, count)
            count = 0
        }
    }

    result = Math.max(count, result)
    process.stdout.write(result.toString());
});