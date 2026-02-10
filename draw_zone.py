import cv2
import numpy as np

zone_fixed = False
zone_points = []
person_in_figure = False

def detect_zone(event, x, y, flags, param):
    global zone_points, zone_fixed
    if zone_fixed:
        return
    if event == cv2.EVENT_LBUTTONDOWN and len(zone_points) <= 3:
        zone_points.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN and zone_points:
        zone_points.pop()

def zone_apply_or_delete(key):
    global zone_fixed, zone_points
    if key == 13:
        zone_fixed = True
    elif key in (ord("r"), ord("R")):
        zone_points.clear()
        zone_fixed = False

def draw_zone(frame):
    for point in zone_points:
        cv2.circle(frame, point, 5, (0, 0, 255), -1)

    if len(zone_points) > 1:
        for i, point in enumerate(zone_points):
            start = point
            end = zone_points[(i + 1) % len(zone_points)]
            cv2.line(frame, start, end, (0, 0, 255), 2)
    return frame

def check_zone(results):
    global zone_points, person_in_figure
    person_xy = []
    if len(zone_points) >= 3:
        polygon = np.array(zone_points, dtype=np.int32)
    else:
        polygon = None

    for result in results:
        for box in result.boxes.xywh:
            x_center, y_center, w, h = box
            x1 = int(x_center - w / 2)
            y1 = int(y_center - h / 2)
            x2 = int(x_center + w / 2)
            y2 = int(y_center + h / 2)

            inside = False
            if polygon is not None:
                if cv2.pointPolygonTest(polygon, (float(x_center), float(y_center)), False) >= 0:
                    inside = True
            person_xy.append(((x1, y1), (x2, y2), inside))
    person_in_figure = any(p[2] for p in person_xy)
    return person_in_figure, person_xy