const request = new XMLHttpRequest()

request.open('GET', '/fetch-data', true)
request.onload = function () {

    const data = JSON.parse(this.response)

    if (request.status >= 200 && request.status < 400) {
        console.log(data);
    } else {
        console.log('error')
    }
}

request.send()