/*
* Format: (xxx) xxx-xxxx
*/

function createPhoneNumber(numbers){
    const s1 = (numbers.slice(0, 3).map(x => x.toString())).join('');
    const s2 = (numbers.slice(3, 6).map(x => x.toString())).join('');
    const s3 = (numbers.slice(6).map(x => x.toString())).join('');
    return `(${s1}) ${s2}-${s3}`
}