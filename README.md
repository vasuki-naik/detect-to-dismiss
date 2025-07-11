![License: MIT]
🛏️ Photo Alarm Clock ⏰📸

A fun and effective alarm clock for lazy people who can't stop snoozing!
🔥 What Is It?

Photo Alarm Clock is a Python-based smart alarm system that won’t turn off until you re-upload a photo of a specific object (like your toothbrush, water bottle, or even your face 😅). This motivates you to get out of bed and prove you’re up — no more lazy snoozing!

    Think of it as your alarm’s way of saying, "I’ll believe you’re awake when I see proof!"

🧠 Key Features

    ⏰ Custom Alarm Time — Set your desired wake-up time

    📸 Capture a Reference Object — Take a photo when setting the alarm

    🚫 No Dismiss Until Matched — Alarm rings continuously until a live photo matches the original one

    🤖 Computer Vision Powered — Uses ORB feature detection to compare images

    🎵 Looping Alarm Sound — Keeps ringing until the match is confirmed

💻 Technologies Used

    Python 🐍

    OpenCV (cv2) 📷

    Pygame 🎵

    ORB (Oriented FAST and Rotated BRIEF) for image matching

🚀 How It Works

    Set Alarm Time — Enter the time you want the alarm to ring.

    Take a Reference Photo — Point your webcam to an object and press 's' to save it.

    Wait for Alarm — The program waits until the set time.

    Alarm Rings — You must take a live photo of the same object.

    Matching Process — If the photos match (using ORB features), the alarm turns off. If not, try again!

🖼️ Example Use Case

Set your toothbrush as the reference object. In the morning, go to the bathroom, show your toothbrush to the camera — only then does the alarm stop. You’re already half-ready for the day!
🛠️ How to Run It

    Clone this repo

git clone https://github.com/your-username/photo-alarm-clock.git
cd photo-alarm-clock

Install dependencies

pip install opencv-python pygame

Make sure you have a .mp3 alarm sound file named alarm_sound.mp3 in the same directory.

Run the program

    python alarm.py

⚠️ Notes

    Works best in consistent lighting. Try not to change the object's background too much.

    Match thresholds (match_ratio > 0.2 and good_matches > 40) can be adjusted depending on your object.

🎯 Future Improvements

    GUI version with buttons and timers

    Face recognition-based wake-up

    Mobile version using camera and alarm APIs

    Cloud sync to track your waking habits

🤝 Contributing

Pull requests are welcome! Feel free to open issues for suggestions or bugs.
📜 License

This project is licensed under the MIT License.
