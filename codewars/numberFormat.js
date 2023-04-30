/*
* Format: (xxx) xxx-xxxx
*/

function createPhoneNumber1(numbers) {
    const s1 = (numbers.slice(0, 3).map(x => x.toString())).join('');
    const s2 = (numbers.slice(3, 6).map(x => x.toString())).join('');
    const s3 = (numbers.slice(6).map(x => x.toString())).join('');
    return `(${s1}) ${s2}-${s3}`
}

function createPhoneNumber2(numbers) {
  return numbers.join('').replace(/(...)(...)(.*)/, '($1) $2-$3');
}

function createPhoneNumber3(numbers) {
   return numbers.reduce((p,c) => p.replace('x',c), "(xxx) xxx-xxxx");
}