const spinnerTimeout = async function (request, showSpinner, hideSpinner) {

    const promise1 = request();
    const promise2 = new Promise(() => {

        setTimeout(() => {
            showSpinner();
        }, 250)

        setTimeout(() => {
            hideSpinner();
        }, 1000)
    })

    Promise.all([promise1, promise2]).then(() => {
        hideSpinner();
    })
}
