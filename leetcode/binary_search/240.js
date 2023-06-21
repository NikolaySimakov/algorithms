/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    
    const n = matrix.length;
    let row = 0;
    let col = matrix[0].length - 1;

    while (row < n && col >= 0) {

        const mid = matrix[row][col];

        if (mid === target) {
            return true;
        }

        if (mid > target) {
            col--;
        } else {
            row++;
        }

    }

    return false
};