# Lumberjack Telegram Bot

This repository contains two main projects:

## 1. Lumberjack Robot
An automated script that plays the Lumberjack game in Telegram using image processing and PyAutoGUI.

### Features
- Automatically detects game state using pixel color detection
- Plays the game by simulating keyboard inputs
- Real-time decision making based on visual cues

### Requirements
- Python 3.6+
- pyautogui
- win32gui (for Windows)

### Usage
1. Open the Lumberjack game in your browser or Telegram
2. Run the script: `python lumberjack.py`
3. The bot will automatically start playing after a 3-second delay

## 2. Simple Todo Bot
A Telegram bot that manages todo lists for users with SQLite database storage.

### Features
- Add todo items by sending text messages
- Remove completed items using inline keyboard
- Personal todo lists for each user
- Persistent storage with SQLite

### Requirements
- Python 3.6+
- requests
- A Telegram Bot Token (from @BotFather)

### Setup
1. Create a bot using @BotFather on Telegram
2. **Configure the Bot**:
   - Copy `Simple Bot/Main/config.example.py` to `Simple Bot/Main/config.py`
   - Replace `YOUR_BOT_TOKEN_HERE` with your actual bot token
3. Run the bot: `python todobot.py`

## Installation

```bash
# Clone the repository
git clone https://github.com/armansheikhhosseini/Lumberjack_Telegram_Bot.git
cd Lumberjack_Telegram_Bot

# Install dependencies
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Arman Sheikhhosseini
