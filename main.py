import cv2
from capture.screen import capture
from detector.yolo_detector import detector
from utils.draw import draw_ui, draw_fps
from utils.fps import get_fps
from draw_zone import detect_zone, draw_zone, zone_apply_or_delete, check_zone

cv2.namedWindow("YOLO")
cv2.setMouseCallback("YOLO", detect_zone)

def main():
    while True:
        frame = capture()
        results = detector(frame)
        frame = draw_zone(frame)
        person_in_figure, person_xy = check_zone(results)
        frame = draw_ui(frame, results, person_xy)
        print(person_in_figure, person_xy)
        fps = get_fps()
        frame = draw_fps(frame, fps)
        cv2.imshow("YOLO", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        elif key == 13:
            zone_apply_or_delete(key)
        elif key == ord("r"):
            zone_apply_or_delete(key)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
