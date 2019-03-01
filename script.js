openSocket = () => {
    let uri = "ws://" + window.location.hostname + ":8585";
    socket = new WebSocket(uri);
    let msg = document.getElementById("msg");
    socket.addEventListener('open', (e) => {
        document.getElementById("status").innerHTML = "Opened";
    });
    socket.addEventListener('message', (e) => {
        let ctx = msg.getContext("2d");
        let image = new Image();
        image.src = URL.createObjectURL(e.data);
        image.addEventListener("load", (e) => {
            ctx.drawImage(image, 0, 0, msg.width, msg.height);
        });
    });
    // setupPointer()
}

// setupPointer = () => {
//     let msg = document.getElementById("msg");
//     msg.requestPointerLock = msg.requestPointerLock;
//     document.exitPointerLock = document.exitPointerLock;
//     msg.addEventListener("click", () => {
//         msg.requestPointerLock();
//     });
//     document.addEventListener('pointerlockchange', () => {
//         if (document.pointerLockElement === msg) {
//           console.log('The pointer lock status is now locked');
//           document.addEventListener("mousemove", updatePosition, false);
//         } else {
//           console.log('The pointer lock status is now unlocked');
//           document.removeEventListener("mousemove", updatePosition, false);
//         }
//     }, false);
// }

// updatePosition = (e) => {
//     console.log(e.movementX);
//     console.log(e.movementY);
//     socket.send(e.movementX);
//     socket.send(e.movementY);
// }