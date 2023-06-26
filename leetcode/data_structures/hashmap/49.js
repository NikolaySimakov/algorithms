/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const resObj = {}
    
    for (let s of strs) {
        const ss = s.split('').sort().join('')
        if (resObj[ss] !== undefined) {
            resObj[ss].push(s)
        } else {
            resObj[ss] = [s]
        }
    }

    return Object.values(resObj)
};