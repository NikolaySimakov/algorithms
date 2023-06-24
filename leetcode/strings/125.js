/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {

    const onlyLettersAndNumbers = (str) => /^[A-Za-z0-9]*$/.test(str);
    const reverseString = (str) => str.split("").reverse().join("");

    let res = '';
    for (let char of s.toLowerCase()) {
        if (onlyLettersAndNumbers(char)) {
            res += char;
        }
    }

    return reverseString(res) === res;
};