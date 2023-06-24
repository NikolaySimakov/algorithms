/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let l = 0, r = nums.length - 1;
    const res = [];

    while (l <= r) {
        if (Math.abs(nums[r]) >= Math.abs(nums[l])) {
            res.unshift(nums[r] * nums[r]);
            r--;
        } else {
            res.unshift(nums[l] * nums[l]);
            l++;
        }
    }

    return res;
};