# ⏰ Object Photo-Based Alarm Clock

This Python alarm app only turns off when you show the *same object photo* that was saved before the alarm!

## 🔧 Features
- Set alarm time (HH:MM)
- Take reference photo via webcam
- Alarm rings at set time
- Stops only when the matching object is shown again via webcam

## 💻 Built With
- Python 3
- OpenCV
- Pygame

## 📸 How It Works
1. App asks for alarm time
2. You take a photo of an object (e.g. a cup)
3. When the alarm rings, you must show the *same object*
4. If matched — alarm stops!

## 🚀 How to Run

```bash
pip install opencv-python pygame
python main.py