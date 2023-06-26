// Не секрет, что некоторые программисты очень любят путешествовать. Хорошо всем известный программист Петя тоже очень любит путешествовать, посещать музеи и осматривать достопримечательности других городов.
// Для перемещений между из города в город он предпочитает использовать машину. При этом он заправляется только на станциях в городах, но не на станциях по пути. Поэтому он очень аккуратно выбирает маршруты, чтобы машина не заглохла в дороге. А ещё Петя очень важный член команды, поэтому он не может себе позволить путешествовать слишком долго. Он решил написать программу, которая поможет ему с выбором очередного путешествия. Но так как сейчас у него слишком много других задач, он попросил вас помочь ему.
// Расстояние между двумя городами считается как сумма модулей разности по каждой из координат. Дороги есть между всеми парами городов.

const bfs = (s, adj) => {
    const cost = new Array(adj.length).fill(-1)
    const queue = [s]
    cost[s] = 0

    while (queue.length > 0) {
        const v = queue.shift()

        for (const w of adj[v]) {
            if (cost[w] === -1) {
                queue.push(w)
                cost[w] = cost[v] + 1
            }
        }
    }
}

const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin
})

let lines = []

rl.on('line', (line) => {
    lines.push(line)
}).on('close', () => {

    const adj = lines.slice(1, -2).map(x => x.split(' ').map(y => +y))
    const cost = +(lines[lines.length - 2])
    const [start, end] = lines[lines.length - 1].split(' ').map(x => +x)
    const ans = bfs(start, adj)
    if (cost >= ans[end]) {
        process.stdout.write(ans[end].toString())
    } else {
        process.stdout.write('-1')
    }
})