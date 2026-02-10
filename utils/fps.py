import time

prev_time = None

def get_fps():
    global prev_time
    now = time.time()
    fps = 0
    if prev_time is not None:
        fps = 1 / (now - prev_time)
    prev_time = now
    return fps