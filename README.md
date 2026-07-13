# 🐍 Snake Game with Hand Gesture Control

A Python-based Snake Game that combines the classic Nokia Snake experience with real-time hand gesture recognition. The game uses your webcam to detect hand movements, allowing you to control the snake without using a keyboard.

---

## 🎮 Features

- 🐍 Classic Snake gameplay
- 🖐️ Hand gesture control using webcam
- 📷 Real-time hand tracking with MediaPipe
- 🍎 Random food generation
- 📊 Live score tracking
- 💥 Game Over screen
- 🔄 Restart functionality
- ⚡ Smooth gameplay

---

## 🛠️ Technologies Used

- Python
- Pygame
- OpenCV
- MediaPipe
- NumPy

---

## 📁 Project Structure

```text
MY SNAKE GAME/
│
├── python3/
│   ├── __pycache__/
│   └── muskan/          (Virtual Environment)
│       ├── Include/
│       ├── Lib/
│       ├── Scripts/
│       └── pyvenv.cfg
│
├── gesture_controller.py   # Hand gesture detection
├── snake_game.py           # Snake game logic
├── main.py                 # Main program
├── setup.py                # Project setup
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/my-snake-game.git
```

### 2. Open the project

```bash
cd my-snake-game
```

### 3. Create a virtual environment (Optional)

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install the required libraries

```bash
pip install pygame opencv-python mediapipe numpy
```

### 6. Run the game

```bash
python main.py
```

---

## 🎮 How to Play

1. Launch the game.
2. Allow webcam access.
3. Keep your hand in front of the camera.
4. Move your hand to control the snake.
5. Eat food to increase your score.
6. Avoid hitting the walls or the snake's own body.

---

## 📂 Project Files

| File | Description |
|------|-------------|
| **main.py** | Starts the game |
| **snake_game.py** | Contains the snake game logic |
| **gesture_controller.py** | Detects and processes hand gestures |
| **setup.py** | Project setup configuration |

---

## 📸 Screenshots

Add your gameplay screenshots here.

Example:

```
screenshots/gameplay.png
```

---

## 🔮 Future Improvements

- Save High Score
- Multiple Difficulty Levels
- Background Music
- Sound Effects
- Pause/Resume Game
- Better Gesture Recognition
- Attractive UI
- Different Themes

---

## 💻 Requirements

- Python 3.9 or above
- Webcam
- Pygame
- OpenCV
- MediaPipe
- NumPy

---

## 👩‍💻 Author

**Muskan Chauhan**

- 🎓 Computer Science Graduate
- 🤖 AI Application Developer
- 🐍 Python Developer

---

## ⭐ If you like this project

Please give this repository a **⭐ Star** on GitHub.

---

## 📜 License

This project is developed for educational and learning purposes.
