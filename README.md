# 🛏️ Photo Alarm Clock ⏰📸  
> A fun and effective alarm clock that *refuses to snooze* until it sees proof you're awake!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green)](#)

---

## 📌 About the Project

**Photo Alarm Clock** is a smart, Python-powered alarm system designed to wake up even the laziest of sleepers.  
Instead of just tapping "Snooze", users must **recreate a photo of a chosen object** — only then will the alarm stop ringing.

> Think of it as your alarm saying: “I’ll believe you're awake when you prove it!”

---

## 🧠 Key Features

- ⏰ **Custom Alarm Time** — Set any time to trigger the alarm  
- 📸 **Reference Photo Capture** — Take a photo of any object (like a toothbrush or bottle)  
- 🔄 **Image Matching Required to Dismiss** — Must upload a matching image to stop the alarm  
- 🤖 **Computer Vision-Powered** — Uses ORB feature detection for accurate photo comparison  
- 🔊 **Looping Alarm Sound** — Alarm continues until a valid photo is matched

---

## 💻 Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core programming |
| **OpenCV** | Webcam, photo capture, and image matching |
| **Pygame** | Alarm sound playback |
| **ORB Algorithm** | Feature-based image recognition |

---

## 🚀 How It Works

1. **Set your alarm time** via input prompt
2. **Capture a reference image** of any object
3. At the alarm time, a loud alarm begins playing
4. To stop it, **you must take a new photo of the same object**
5. The new photo is compared using feature-matching. Only a **successful match** stops the alarm

---

## 🖼️ Example Use Case

Imagine you set your **toothbrush** as the reference.  
Next morning, the alarm rings → you **go to the bathroom**, show the same toothbrush to the webcam → the alarm turns off ✅

You're out of bed and on your way — no lazy snoozing!

---

## 🛠️ How to Run It Locally

```bash
# Clone this repository
git clone https://github.com/vasuki-naik/detect-to-dismiss.git
cd detect-to-dismiss

# Install required packages
pip install opencv-python pygame

# Make sure alarm_sound.mp3 is in the same folder

# Run the program
python alarm.py

⚠️ Notes

    Ensure consistent lighting for better image matching.

    Avoid background clutter or drastic object movement.

    You can tweak these match thresholds:

        match_ratio > 0.2

        good_matches > 40

💡 Skills Demonstrated

    Real-time image processing

    Computer vision with ORB feature matching

    Webcam and audio device handling

    User interaction logic

    Problem-solving and creative thinking

📈 Future Enhancements

    ✅ Mobile app version using Flutter or Kotlin

 🤝 Contributing

Contributions are welcome!
Feel free to open an issue or submit a pull request.

📜 License

This project is licensed under the MIT License.
