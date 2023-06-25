var RandomizedSet = function() {
    this.map1 = new Map() // value -> index
    this.map2 = new Map() // index -> value
    this.count = 0
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (this.map1.has(val)) {
        return false
    } else {
        this.map1.set(val, this.count)
        this.map2.set(this.count, val)
        this.count += 1
        return true
    }
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if (this.map1.has(val)) {
        const index = this.map1.get(val)
        this.map1.delete(val)
        if (this.count - 1 !== index) {
            const value = this.map2.get(this.count - 1)
            this.map1.set(value, index)
            this.map2.set(index, value)
            this.map2.delete(this.count - 1)
        }
        this.count -= 1
        return true
    } else {
        return false
    }
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    const index = Math.floor(Math.random() * this.count)
    return this.map2.get(index)
};

/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */