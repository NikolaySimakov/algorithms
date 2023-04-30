/**
 * Write an algorithm that takes an array and moves 
 * all of the zeros to the end, preserving 
 * the order of the other elements.
 */

function moveZeros(arr) {
  const notZeros = arr.filter(x => x !== 0);
  const zeros = arr.filter(x => x === 0);
  return notZeros.concat(zeros);
}