const sysInfo = async () => {
    let headers = new Headers();

    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    headers.append('Origin','http://127.0.0.1:8080');

    const response = await fetch('http://127.0.0.1:8080/info', {
         method: 'GET', // *GET, POST, PUT, DELETE, etc.
         mode: 'cors', // no-cors, *cors, same-origin
         cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
         credentials: 'same-origin', // include, *same-origin, omit
    });
    const myJson = await response.json(); //extract JSON from the http response
    console.log(myJson['currentTime'].toString());
    document.getElementById('date').innerHTML = myJson['currentTime'];
    document.getElementById('proc').innerHTML = myJson['proc'];
    document.getElementById('mem').innerHTML = myJson['mem'];
}


function show() {
     sysInfo();
}
