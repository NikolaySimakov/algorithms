var TimeLimitedCache = function() {
    const map = new Map();
    this.map = map;
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {

    const currTime = new Date();
    currTime.setTime(currTime.getTime() + duration)
    const hasKey = this.map.has(key);
    this.map.set(key, {
        val: value,
        dur: currTime.getTime(),
    });
    return hasKey;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const currTime = new Date();
    const val = this.map.get(key);
    if (val === undefined) {
        return -1;
    } else {
        if (val.dur > currTime.getTime()) {
            return val.val;
        } else {
            this.map.delete(key);
            return -1;
        }
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    const currTime = (new Date()).getTime();
    let counter = 0;
    for (let key of this.map.keys()) {
        if (this.map.get(key).dur >= currTime) {
            counter++;
        }
    }
    return counter;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */