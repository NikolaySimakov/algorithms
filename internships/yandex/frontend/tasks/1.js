const obj = {
    queue: [],
    _max: 0,
    _min: Infinity,
    push(x) {
        this.queue.push(x);

        if (x > this._max) {
            this._max = x;
        }

        if (x < this._min) {
            this._min = x;
        }
    },
    shift() {
        if (this.queue.length !== 0) {
            const val = this.queue.shift();
            if (this.queue.length === 0) {
                this._max = 0;
                this._min = Infinity;
            } else {
                if (val === this._max) {
                    this._max = Math.max(...this.queue);
                } else if (val === this._min) {
                    this._min = Math.min(...this.queue);
                }
            }
            return val;
        }
        return 0
    },
    min() {
        if (this.queue.length !== 0) {
            return this._min
        }
        return 0
    },
    max() {
        if (this.queue.length !== 0) {
            return this._max
        }
        return 0
    }
};

obj.push(2)
obj.push(1)
obj.push(2)
obj.push(3)

console.log(obj.min(), obj.max(), obj.shift())