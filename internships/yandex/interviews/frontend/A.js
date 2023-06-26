// Даны две строки строчных латинских символов: строка J и строка S. Символы, входящие в строку J, — «драгоценности», входящие в строку S — «камни». Нужно определить, какое количество символов из S одновременно являются «драгоценностями». Проще говоря, нужно проверить, какое количество символов из S входит в J.

const readline = require('readline');
 
const rl = readline.createInterface({
    input: process.stdin
});
 
let lines = [];
rl.on('line', (line) => {
    lines.push(line);
}).on('close', () => {
    const [jewels, stones] = lines
    let result = 0;
    for (let i = 0; i < stones.length; i++) {
        if (jewels.includes(stones.charAt(i))) {
            ++result;
        }
    }
    process.stdout.write(result.toString());
});