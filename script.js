openSocket = () => {
    let uri = "ws://" + window.location.hostname + ":8585";
    let socket = new WebSocket(uri);
    let msg = document.getElementById("msg");
    socket.addEventListener('open', (e) => {
        document.getElementById("status").innerHTML = "Opened";
    })
    socket.addEventListener('message', (e) => {
        URL.revokeObjectURL(msg.src);
        urlObject = URL.createObjectURL(e.data);
        msg.src = urlObject;
    });
}