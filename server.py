import http.server as http
import asyncio
import websockets
import multiprocessing
import cv2
import time

# Keep track of our processes
PROCESSES = []

def camera(man):
    cv2.namedWindow("preview")
    print("[LOG] Starting camera")
    vc = cv2.VideoCapture(0)

    if vc.isOpened():
        r, f = vc.read()
    else:
        r = False
    

    while r:
        cv2.imshow("preview", f)
        cv2.waitKey(20)
        r, f = vc.read()
        cv2.putText(f, 
                    str(time.time()), 
                    (100, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, 
                    (255,255,255),
                    2,
                    cv2.LINE_AA)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 30]
        man[0] = cv2.imencode('.jpg', f, encode_param)[1]

# HTTP server handler
def server():
    print("[LOG] Server started")
    server_address = ('0.0.0.0', 8000)
    httpd = http.ThreadingHTTPServer(server_address, http.SimpleHTTPRequestHandler)
    httpd.serve_forever()

def socket(man):
    # Will handle our websocket connections
    async def handler(websocket, path):
        print("[LOG] Socket opened")
        while True:
            time.sleep(0.042) # 24 fps
            await websocket.send(man[0].tobytes())

    print("[LOG] Starting socket handler")
    # Create the awaitable object
    start_server = websockets.serve(ws_handler=handler, host='0.0.0.0', port=8585)
    # Start the server, add it to the event loop
    asyncio.get_event_loop().run_until_complete(start_server)
    # Registered our websocket connection handler, thus run event loop forever
    asyncio.get_event_loop().run_forever()


def main():
    # queue = multiprocessing.Queue()
    manager = multiprocessing.Manager()
    lst = manager.list()
    lst.append(None)
    # Host the page, creating the server
    http_server = multiprocessing.Process(target=server)
    # Set up our websocket handler
    socket_handler = multiprocessing.Process(target=socket, args=(lst,))
    # Set up our camera
    camera_handler = multiprocessing.Process(target=camera, args=(lst,))
    # Add 'em to our list
    PROCESSES.append(camera_handler)
    PROCESSES.append(http_server)
    PROCESSES.append(socket_handler)
    for p in PROCESSES:
        p.start()
    # Wait forever
    while True:
        pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        for p in PROCESSES:
            p.kill()