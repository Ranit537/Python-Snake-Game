# 🐍 Python Snake Game

A classic **Snake Game** built using Python’s Turtle graphics module. Control the snake, eat food, grow longer, and try not to collide with walls or yourself!

---

## 🎮 Features

* 🐍 Smooth snake movement
* 🍎 Random food spawning
* 📈 Score tracking system
* 💥 Collision detection (wall + self)
* 🎯 Real-time gameplay
* ⌨️ Keyboard controls (W A S D)

---

## 📦 Requirements

No external libraries needed ✅
Uses only built-in Python modules:

* turtle
* random
* time

Just make sure Python is installed.

Check Python version:

```
python --version
```

---

## ▶️ How to Run

Clone repository:

```
git clone https://github.com/Ranit537/Python-Snake-Game.git
cd Python-Snake-Game/SnakeGame
```

Run the game:

```
python Game.py
```

---

## 🎮 Controls

| Key | Action     |
| --- | ---------- |
| W   | Move Up    |
| S   | Move Down  |
| A   | Move Left  |
| D   | Move Right |

---

## 📁 Project Structure

```
Python-Snake-Game/
│
├── SnakeGame/
│   ├── Game.py
│   ├── snake.py
│   ├── food.py
│   └── scoreboard.py
│
├── README.md
└── .gitattributes
```

---

## 🧠 How Game Works

Game loop logic:

1. Create screen
2. Spawn snake
3. Spawn food
4. Listen for keyboard input
5. Move snake continuously
6. Detect collisions
7. Increase score when food eaten
8. End game if collision occurs

---

## 🛠 Troubleshooting

**Game window not opening**

* Ensure Python installed correctly

**Controls not working**

* Click game window first, then press keys

**Module error**

* Run file from inside `SnakeGame` folder

---

## 📜 License

This project is open source and free to use.

---

## 👨‍💻 Author

**Ranit537**
GitHub: https://github.com/Ranit537

---

⭐ Star this repo if you enjoyed the game!
