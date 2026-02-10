from mss import mss
import numpy as np

sct = mss()
monitor = sct.monitors[1]

def capture():
    frame = np.array(sct.grab(monitor))[:, :, :3].copy()
    return frame