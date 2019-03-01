# Livestreaming webcam through WebSockets

This is a proof-of-concept demo of using WebSockets to stream a video camera feed through WebSockets, so any browser can access it. 

At the moment, it is very work-in-progress. The stream is coming in as the raw JPEG binary, which is then read as a blob to be displayedd as an image on the page.

The latency is about ~0.1s, but with relatively high CPU usage.

To demo this, make sure you have `opencv-python` and `websockets` installed, and you have Python 3.6+.

# Demo

1. Ensure you have the prerequisites, try `pip install -r requirements.txt`
2. Run `python server.py`
3. Visit `localhost:8000` to view the stream. A corresponding window will also be loaded with the current time.