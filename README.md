# YOLO Zone Detection

This project uses YOLOv8 to detect persons on the screen.
A user-defined polygonal zone can be created interactively.
If the center of a detected person's bounding box is inside the zone,
the bounding box is displayed in red, otherwise in green.

## Features
- Real-time person detection using YOLOv8
- Interactive zone creation using mouse and keyboard
- Visual feedback depending on object position
- FPS counter

## Controls (English keys only)

- Left Mouse Button (LMB) — add a point to the zone
- Right Mouse Button (RMB) — remove the last added point
- ENTER — lock the zone (disables further editing)
- R — reset / clear all points and unlock the zone

## Technologies
- Python
- Ultralytics YOLOv8
- OpenCV
- MSS (screen capture)

## How to run

`bash
pip install -r requirements.txt
python main.py