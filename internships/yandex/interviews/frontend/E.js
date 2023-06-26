// Даны две строки, состоящие из строчных латинских букв. Требуется определить, являются ли эти строки анаграммами, т. е. отличаются ли они только порядком следования символов.

const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
})

function anagram(a, b) {
    if (a.length !== b.length) {
        return 0
    }
    
    const a_obj = {}
    const b_obj = {}
    
    for (let i = 0; i < a.length; i++) {
        a_obj[a[i]] = a_obj[a[i]] === undefined ? 0 : a_obj[a[i]] + 1
        b_obj[b[i]] = b_obj[b[i]] === undefined ? 0 : b_obj[b[i]] + 1
    }

    for (const key of Object.keys(a_obj)) {
        if (a_obj[key] !== b_obj[key]) {
            return 0
        }
    }

    for (const key of Object.keys(b_obj)) {
        if (a_obj[key] !== b_obj[key]) {
            return 0
        }
    }

    return 1
}

let lines = []

rl.on('line', (line) => {
    lines.push(line)
}).on('close', () => {
    const [a, b] = lines
    const res = anagram(a, b)
    process.stdout.write(res.toString())
})
