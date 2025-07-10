import cv2
import time
from datetime import datetime
import pygame

# Initialize sound
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("alarm_sound.mp3")

# Function to take a photo
def take_photo(filename):
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("❌ Webcam not opening!")
        return False
    print(f"📸 Show the object to webcam. Press 's' to save as {filename}")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("⚠ Failed to grab frame")
            break
        cv2.imshow("Webcam", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename, frame)
            print(f"✅ Saved as {filename}")
            break
        elif key == 27:
            print("❌ Cancelled")
            break

    cam.release()
    cv2.destroyAllWindows()
    return True

# Function to compare two images using ORB and ratio test
def compare_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path, 0)
    img2 = cv2.imread(img2_path, 0)

    if img1 is None or img2 is None:
        print("❌ Image missing or unreadable")
        return 0, 0, 0

    orb = cv2.ORB_create(nfeatures=1000)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    if des1 is None or des2 is None:
        print("⚠ No descriptors found")
        return 0, len(kp1), len(kp2)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply Lowe's ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    return len(good_matches), len(kp1), len(kp2)

# Ask for alarm time
alarm_time = input("⏰ Enter alarm time (HH:MM): ")

# Take reference image
print("🧾 Let's capture the object you'll show tomorrow!")
take_photo("reference.jpg")

print(f"🕒 Alarm set for {alarm_time}. Waiting...")

# Wait for alarm time
while True:
    now = datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("🔔 Wake up! Alarm ringing!")
        pygame.mixer.music.play(-1)  # Loop alarm sound

        while True:
            input("📸 Press Enter to take a photo of the same object...")

            success = take_photo("current.jpg")
            if not success:
                continue

            diff, kp1_count, kp2_count = compare_images("reference.jpg", "current.jpg")
            match_ratio = diff / min(kp1_count, kp2_count) if min(kp1_count, kp2_count) > 0 else 0

            print(f"📊 Good Matches: {diff}")
            print(f"📈 Match Ratio: {match_ratio:.2f}")

            # Adjust these thresholds based on your object and lighting
            if diff > 40 and match_ratio > 0.2:
                print("✅ Match successful! Alarm off.")
                pygame.mixer.music.stop()
                break
            else:
                print("❌ Not matched. Try again.")

        break

    time.sleep(10)
    