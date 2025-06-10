import cv2
import mediapipe as mp
import numpy as np
import urllib.request

# Load transparent images directly from URLs
def load_filter_from_url(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype=np.uint8)
    return cv2.imdecode(image, cv2.IMREAD_UNCHANGED)

# Filter URLs (PNG with transparency)
filter_urls = [
    "https://i.ibb.co/QXr8SPc/sunglasses.png",     # Sunglasses
    "https://i.ibb.co/98mN2rp/dog-nose.png",        # Dog nose
    "https://i.ibb.co/Nr98kvJ/flower-crown.png"     # Flower crown
]

# Load filters from web
filters = [load_filter_from_url(url) for url in filter_urls]
current_filter = 0

# Initialize MediaPipe
mp_face = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
face_mesh = mp_face.FaceMesh(max_num_faces=1)
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Overlay transparent PNG
def overlay_transparent(bg, overlay, x, y, scale=1):
    if overlay is None: return bg
    oh, ow = overlay.shape[:2]
    overlay = cv2.resize(overlay, (int(ow * scale), int(oh * scale)))
    b, g, r, a = cv2.split(overlay)
    mask = a / 255.0
    h, w = overlay.shape[:2]

    if x < 0 or y < 0 or y + h > bg.shape[0] or x + w > bg.shape[1]:
        return bg

    roi = bg[y:y + h, x:x + w]
    for c in range(3):
        roi[..., c] = roi[..., c] * (1 - mask) + [b, g, r][c] * mask
    bg[y:y + h, x:x + w] = roi
    return bg

# Count raised fingers (hand gesture)
def count_fingers(lms):
    finger_tips = [8, 12, 16, 20]
    count = 0
    for tip in finger_tips:
        if lms.landmark[tip].y < lms.landmark[tip - 2].y:
            count += 1
    return count

# Start camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hand and update filter index
    hand_result = hands.process(rgb)
    if hand_result.multi_hand_landmarks:
        for hand_landmarks in hand_result.multi_hand_landmarks:
            finger_count = count_fingers(hand_landmarks)
            if 1 <= finger_count <= 3:
                current_filter = finger_count - 1

    # Detect face
    face_result = face_mesh.process(rgb)
    if face_result.multi_face_landmarks:
        for landmarks in face_result.multi_face_landmarks:
            h, w, _ = frame.shape
            lm = landmarks.landmark
            lx, ly = int(lm[33].x * w), int(lm[33].y * h)
            rx, ry = int(lm[263].x * w), int(lm[263].y * h)
            nx, ny = int(lm[1].x * w), int(lm[1].y * h)
            fx, fy = int(lm[10].x * w), int(lm[10].y * h)

            # Apply selected filter
            if current_filter == 0:  # Sunglasses
                eye_w = rx - lx
                frame = overlay_transparent(frame, filters[0], lx - 20, ly - 30, scale=eye_w / filters[0].shape[1] * 2)
            elif current_filter == 1:  # Dog nose
                frame = overlay_transparent(frame, filters[1], nx - 25, ny, scale=0.5)
            elif current_filter == 2:  # Flower crown
                frame = overlay_transparent(frame, filters[2], fx - 100, fy - 130, scale=1.5)

    cv2.putText(frame, f"Filter: {current_filter + 1}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv2.imshow("Snapchat Filters with Hand Gestures", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
