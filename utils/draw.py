import cv2

def draw_ui(frame, results, person_xy):
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())
            class_id = int(box.cls[0].item())
            confidence = float(box.conf[0].item())
            label = f"{result.names[class_id]} {confidence:.2f}"

    for corner1, corner2, inside in person_xy:
        if inside:
            cv2.rectangle(frame, corner1, corner2, (0, 0, 255), 2)
        else:
            cv2.rectangle(frame, corner1, corner2, (0, 255, 0), 2)

    return frame

def draw_fps(frame, fps):
    cv2.putText(frame, f"FPS: {fps:.1f}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame
