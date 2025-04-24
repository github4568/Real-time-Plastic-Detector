import cv2
import numpy as np
import urllib.request
from ultralytics import YOLO

# Load your trained YOLO model (replace with your model path)
model = YOLO("best.pt")  # Make sure best.pt is in the same folder or give full path

# Replace with your phone IP and port (from IP Webcam app)
url = 'http://<your ip address>/shot.jpg'

while True:
    try:
        # Capture frame from IP webcam
        img_resp = urllib.request.urlopen(url)
        img_np = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        frame = cv2.imdecode(img_np, -1)

        # Run detection
        results = model(frame)[0]

        # Draw boxes on the frame
        annotated_frame = results.plot()

        # Show the annotated frame
        cv2.imshow("Plastic Detector", annotated_frame)

        # Break on pressing 'q'
        if cv2.waitKey(1) == ord('q'):
            break

    except Exception as e:
        print(f"Error: {e}")
        break

cv2.destroyAllWindows()
