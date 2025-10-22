# jagwargameplay
# 🐆 Jaguar Hunt Game

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![Pygame](https://img.shields.io/badge/pygame-2.0%2B-green)
![License](https://img.shields.io/badge/license-MIT-orange)
![Status](https://img.shields.io/badge/status-active-success)

**An exciting 2D arcade-style hunting game built with Python and Pygame!**

[Features](#features) • [Installation](#installation) • [How to Play](#how-to-play) • [Screenshots](#screenshots) • [Contributing](#contributing)

</div>

---

## 📖 Description

**Jaguar Hunt** is a fast-paced arcade game where you control a mighty jaguar hunting for prey in the jungle. Navigate through obstacles, catch various animals using your pounce ability, and survive as long as possible while racking up your high score!

Built entirely with Python and Pygame, this game features custom sprite animations, particle effects, progressive difficulty, and smooth gameplay mechanics.

---

## ✨ Features

### 🎮 Gameplay
- **Smooth Movement Controls** - Use Arrow Keys or WASD for precise control
- **Pounce Mechanic** - Timed special ability to catch prey
- **Multiple Prey Types** - Hunt rabbits, deer, and monkeys
- **Dynamic Obstacles** - Avoid dangerous trees while hunting
- **Progressive Difficulty** - Game gets harder as you survive longer
- **Lives System** - Three chances to prove your hunting skills

### 🎨 Graphics & Effects
- **Custom Animated Sprites** - Hand-drawn jaguar with realistic movements
- **Particle Effects** - Visual feedback for catching prey and taking damage
- **Smooth Animations** - Fluid movement and tail animations
- **Colorful UI** - Clean interface with score, lives, and cooldown indicators

### 🏆 Game Modes
- **Main Menu** - Start screen with instructions
- **Pause System** - Take a break without losing progress
- **Game Over Screen** - View final score and high score
- **High Score Tracking** - Beat your personal best!

---

## 📸 Screenshots

### Main Menu
```
┌─────────────────────────────────────┐
│                                     │
│         🐆 JAGUAR HUNT 🐆           │
│                                     │
│       Press SPACE to Start          │
│                                     │
│           Controls:                 │
│    Arrow Keys / WASD - Move         │
│         SPACE - Pounce              │
│          ESC - Pause                │
│                                     │
│    Hunt prey, avoid obstacles!      │
│                                     │
└─────────────────────────────────────┘
```

*The welcoming main menu with clear instructions*

---

### Gameplay Screen
```
┌─────────────────────────────────────────────────────┐
│ Score: 150        Lives: 3         High: 420        │
│                                                     │
│            🌳                    🐇                 │
│                                                     │
│                  🐆 (Jaguar with golden aura)      │
│         🌳                                          │
│                        🦌                           │
│                                                     │
│               ░░░░░░ POUNCE READY! ░░░░░░          │
└─────────────────────────────────────────────────────┘
```

*Intense hunting action with prey and obstacles*

---

### Pounce Action
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│                   ✨✨✨✨✨                        │
│              ✨   🐆 💫   ✨                        │
│           ✨  (Golden Glow) 🐇  ✨                  │
│                   ✨✨✨✨✨                        │
│                                                     │
│         Particles explode on successful catch!      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

*Spectacular visual effects when catching prey*

---

### Game Over Screen
```
┌─────────────────────────────────────┐
│                                     │
│          🔴 GAME OVER 🔴            │
│                                     │
│        Final Score: 420             │
│        High Score: 550              │
│                                     │
│       Press R to Restart            │
│                                     │
└─────────────────────────────────────┘
```

*See your achievements and try again*

---

## 🎯 Prey Types

| Prey | Points | Description | Visual |
|------|--------|-------------|--------|
| **Rabbit** 🐇 | 10 | Fast and nimble, moves quickly | White with long ears |
| **Deer** 🦌 | 10 | Medium speed, good target | Brown with antlers |
| **Monkey** 🐒 | 10 | Unpredictable movement | Brown with curved tail |

---

## 🚧 Obstacles

| Obstacle | Damage | Description | Visual |
|----------|--------|-------------|--------|
| **Tree** 🌳 | 1 Life | Solid obstacle in your path | Brown trunk with green foliage |

---

## 💻 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/jaguar-hunt-game.git
cd jaguar-hunt-game
```

### Step 2: Install Dependencies
```bash
pip install pygame
```

Or use requirements.txt:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Game
```bash
python jaguar_game.py
```

---

## 🎮 How to Play

### Controls

| Key | Action |
|-----|--------|
| **Arrow Keys** or **WASD** | Move the jaguar in 4 directions |
| **SPACE** | Activate pounce to catch prey |
| **ESC** | Pause/Unpause the game |
| **R** | Restart after game over |

### Gameplay Tips

1. **🎯 Timing is Everything** - Wait for the right moment to pounce on prey
2. **👀 Watch the Cooldown** - Your pounce ability needs time to recharge
3. **🌳 Avoid Obstacles** - Trees will damage you and cost lives
4. **💨 Keep Moving** - Stay mobile to catch more prey and dodge obstacles
5. **📈 Score Strategy** - Chain catches quickly for higher scores
6. **⚡ Golden Glow** - When pouncing, you have a golden aura - that's your catching window!

### Objective

- **Catch as many prey animals as possible** using your pounce ability
- **Avoid tree obstacles** that reduce your lives
- **Survive as long as possible** while the difficulty increases
- **Beat your high score** and become the ultimate jungle hunter!

---

## 🎨 Game Mechanics

### Pounce System
The pounce is your primary hunting tool:
- ⏱️ **Duration**: 0.25 seconds of active hunting
- 🔄 **Cooldown**: 0.5 seconds recharge time
- ✨ **Visual Effect**: Golden aura and particle effects
- 🎯 **Function**: Only works during pounce - time it perfectly!

### Difficulty Progression
- Game starts at a moderate pace
- Every 5 seconds, spawn rate increases
- More obstacles and prey appear simultaneously
- Tests your reflexes and strategic thinking

### Scoring System
- Each prey caught: **+10 points**
- No score for missed prey
- High score persists across game sessions

---

## 📂 Project Structure

```
jaguar-hunt-game/
│
├── jaguar_game.py          # Main game file (500+ lines)
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
│
└── screenshots/           # Game screenshots
    ├── menu.png
    ├── gameplay.png
    ├── pounce.png
    └── gameover.png
```

---

## 🔧 Technical Details

### Built With
- **Python 3.7+** - Programming language
- **Pygame 2.0+** - Game development library

### Key Components

#### Classes
- `Jaguar` - Player character with movement and pounce mechanics
- `Prey` - Various huntable animals (rabbit, deer, monkey)
- `Obstacle` - Hazardous trees
- `Particle` - Visual effects system
- `Game` - Main game loop and state management

#### Game States
- `MENU` - Main menu screen
- `PLAYING` - Active gameplay
- `PAUSED` - Game paused
- `GAME_OVER` - End screen with score

### Performance
- **60 FPS** smooth gameplay
- Efficient sprite management
- Optimized collision detection
- Low memory footprint

---

## 🎥 Gameplay Demo

```
Frame 1: Jaguar spots a rabbit
  🐆 ────────▶ 🐇

Frame 2: Player presses SPACE to pounce
  ✨🐆✨ ─────▶ 🐇

Frame 3: Successful catch with particle explosion!
  ✨💥✨ Score +10!

Frame 4: Avoid the incoming tree obstacle!
      🐆
         ↓
  🌳 ◀────────────
```

---

## 🚀 Future Enhancements

### Planned Features
- [ ] 🔊 Sound effects and background music
- [ ] 🏆 Achievement system
- [ ] 💾 Save/load game progress
- [ ] 🎨 Multiple jungle environments
- [ ] 🐾 Power-ups (speed boost, invincibility)
- [ ] 📊 Statistics tracking (total catches, accuracy)
- [ ] 🎯 Combo system for consecutive catches
- [ ] 🌙 Day/night cycle
- [ ] 🏅 Online leaderboard
- [ ] 🎮 Gamepad support

### Community Requests
- Boss battles with larger prey
- Different jaguar skins
- Multiplayer mode
- Mobile version

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines
- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Test your changes thoroughly
- Update README if adding new features
- Keep commits focused and descriptive

---

## 🐛 Bug Reports

Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- System info (OS, Python version, Pygame version)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Jaguar Hunt Game

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- Inspired by classic arcade hunting games
- Built with the amazing Pygame community
- Thanks to all contributors and testers
- Special thanks to the Python community

---

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/jaguar-hunt-game?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/jaguar-hunt-game?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yourusername/jaguar-hunt-game?style=social)

---

## 📞 Support

- 📧 Email: support@jaguarhunt.com
- 💬 Discord: [Join our community](https://discord.gg/jaguarhunt)
- 📖 Wiki: [Game Wiki](https://github.com/yourusername/jaguar-hunt-game/wiki)

---

## 🎮 Enjoy the Hunt!

<div align="center">

**If you enjoy this game, please consider giving it a ⭐ star on GitHub!**

Made with ❤️ and Python
