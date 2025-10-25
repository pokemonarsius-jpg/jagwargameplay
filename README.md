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
│        🐆 JAGUAR HUNT 🐆           │
│                                     │
│       Press SPACE to Start          │
│       Press ESC to Quit             │
│                                     │
│    Use Arrow Keys or WASD to Move   │
│    Press SPACEBAR to Pounce         │
│                                     │
└─────────────────────────────────────┘
```

### Gameplay
```
┌─────────────────────────────────────┐
│  Score: 150    Lives: ♥♥♥          │
│  High Score: 420                    │
├─────────────────────────────────────┤
│          🌳                         │
│    🐰              🐆              │
│              🌳                     │
│         🦌                          │
│                      🌳            │
│    🌳        🐵                     │
└─────────────────────────────────────┘
│  Pounce Ready: ▓▓▓▓▓▓░░░░         │
└─────────────────────────────────────┘
```

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step-by-Step Guide

1. **Clone the repository**
```bash
git clone https://github.com/pokemonarsius-jpg/jagwargameplay.git
cd jagwargameplay
```

2. **Install required packages**
```bash
pip install pygame
```

Or use requirements.txt:
```bash
pip install -r requirements.txt
```

3. **Run the game**
```bash
python main.py
```

---

## 🎮 How to Play

### Controls
| Action | Keys |
|--------|------|
| Move Up | ↑ or W |
| Move Down | ↓ or S |
| Move Left | ← or A |
| Move Right | → or D |
| Pounce | SPACEBAR |
| Pause | P or ESC |
| Quit | ESC (on menu) |

### Gameplay Instructions

1. **Objective**: Hunt as many prey animals as possible while avoiding obstacles

2. **Movement**: Use arrow keys or WASD to move your jaguar around the screen

3. **Pounce**: Press SPACEBAR to perform a special pounce attack
   - Pounce has a cooldown period
   - Use it strategically to catch fast-moving prey
   - The cooldown bar shows when you can pounce again

4. **Scoring**:
   - 🐰 Rabbit: 10 points
   - 🦌 Deer: 20 points
   - 🐵 Monkey: 30 points

5. **Lives**: You have 3 lives
   - Colliding with trees costs 1 life
   - Game ends when all lives are lost

6. **Difficulty**: The game progressively gets harder
   - Prey moves faster over time
   - More obstacles appear
   - Adapt your strategy!

---

## 🛠️ VS Code Development Setup

This project includes pre-configured VS Code workspace settings for an optimal development experience. The `.vscode` directory contains configurations that enhance productivity and maintain code quality.

### Included VS Code Features

✅ **Auto-save enabled** (1 second delay)
- Changes are automatically saved after 1 second of inactivity
- Never lose your work!

✅ **Format on save**
- Code is automatically formatted when you save
- Maintains consistent code style

✅ **Auto import organization**
- Python imports are automatically sorted and organized
- Removes unused imports

✅ **Bracket pair colorization**
- Matching brackets are colored for easy identification
- Helps prevent syntax errors

✅ **Spell checker configured**
- Catches typos in comments and strings
- Improves documentation quality

✅ **Git integration**
- Built-in source control
- Easy commit, push, and pull operations

✅ **Docker support**
- Ready for containerized development
- Consistent environment across machines

✅ **Live reload**
- See changes instantly during development
- Speeds up the development cycle

✅ **Debug configurations ready**
- Pre-configured Python debugging
- Set breakpoints and inspect variables

### Recommended Extensions

The workspace includes recommendations for VS Code extensions:
- **Python** - IntelliSense, linting, debugging
- **Pylint** - Python code analysis
- **autopep8** - Code formatting
- **GitLens** - Enhanced Git capabilities

### Using the VS Code Setup

1. Open the project folder in VS Code:
```bash
code jagwargameplay
```

2. Install recommended extensions when prompted

3. The workspace settings will be automatically applied

4. Start coding with enhanced productivity!

---

## 🏗️ Project Structure

```
jagwargameplay/
│
├── main.py              # Main game entry point
├── game.py              # Core game logic
├── player.py            # Jaguar player class
├── prey.py              # Prey animals classes
├── obstacle.py          # Obstacle classes
├── particle.py          # Particle effects system
├── constants.py         # Game constants and settings
├── utils.py             # Utility functions
│
├── assets/              # Game assets
│   ├── sprites/         # Character and object sprites
│   ├── sounds/          # Sound effects and music
│   └── fonts/           # Custom fonts
│
├── .vscode/             # VS Code workspace settings
│   ├── settings.json    # Editor configurations
│   └── launch.json      # Debug configurations
│
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── LICENSE              # MIT License
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `pygame not found`
```bash
# Solution: Install pygame
pip install pygame
```

**Issue**: Game runs slowly
- Solution: Close other applications
- Check your Python version (3.7+ recommended)
- Update your graphics drivers

**Issue**: No sound
- Check system volume
- Ensure pygame.mixer is initialized
- Verify sound files are in assets/sounds/

**Issue**: Sprite images not loading
- Verify assets/sprites/ directory exists
- Check file paths in code
- Ensure image files are in correct format (PNG recommended)

---

## 🤝 Contributing

We love contributions! Here's how you can help:

### How to Contribute

1. **Fork the repository**
2. **Create a new branch**
```bash
git checkout -b feature/amazing-feature
```
3. **Make your changes**
4. **Commit with descriptive message**
```bash
git commit -m 'Add amazing feature'
```
5. **Push to your branch**
```bash
git push origin feature/amazing-feature
```
6. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation if needed
- Keep commits atomic and well-described

### Areas for Contribution

- 🎨 New sprite designs
- 🎵 Sound effects and music
- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🌍 Translations
- ⚡ Performance optimizations

### Reporting Bugs

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
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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

</div>
