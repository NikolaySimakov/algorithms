/**
 * @param {number} millis
 */
async function sleep(millis) {
    const promise = new Promise((resolve, _) => {
        setTimeout(() => { resolve(millis) }, millis);
    })
    return promise
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */