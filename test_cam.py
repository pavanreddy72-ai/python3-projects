import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Camera blocked! Go to Chromebook Settings > Linux > Manage USB Devices.")
else:
    print("SUCCESS: Camera is working! (Press 'q' to quit)")

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()