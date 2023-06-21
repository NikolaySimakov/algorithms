/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    if (n === 1) {
        return "1";
    } else {
        let s = countAndSay(n - 1);
        let counter = 1;
        let lastVal = s.charAt(0);
        let res = '';

        for (let i = 1; i < s.length; i++) {
            if (s[i] === lastVal) {
                counter++;
            } else {
                res += counter.toString() + lastVal;
                lastVal = s[i];
                counter = 1;
            }
        }
        res += counter.toString() + lastVal;
        return res;
    }
};