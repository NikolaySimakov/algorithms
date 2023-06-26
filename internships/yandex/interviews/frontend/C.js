// Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.

// Желательно получить решение, которое не считывает входной файл целиком в память, т.е., использует лишь константный объем памяти в процессе работы.

const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin
})

const values = new Set()
let flag = false
rl.on('line', (num) => {
    if (flag) {
        values.add(num)
    } else {
        flag = true
    }
}).on('close', () => {
    for (let value of Array.from(values)) {
        process.stdout.write(value + '\n');
    }
})
