# Lumberjack Game Bot

This Python script automatically plays the Lumberjack game in Telegram using image processing and keyboard automation.

## How it Works

The bot uses pixel color detection to identify when branches appear on either side of the tree. It then simulates keyboard inputs to move the lumberjack to the safe side before cutting.

## Features

- **Automatic gameplay**: No manual intervention required once started
- **Real-time decision making**: Analyzes game state 60+ times per second
- **Visual feedback**: Console output shows detected colors and decisions
- **Error handling**: Graceful handling of interruptions and errors

## Requirements

- Python 3.6 or higher
- Windows OS (uses win32gui for pixel detection)
- pyautogui library for keyboard simulation

## Installation

```bash
pip install pyautogui pywin32
```

## Usage

1. Open the Lumberjack game in your browser or Telegram
2. Position the game window so it's visible
3. Run the script:
   ```bash
   python lumberjack.py
   ```
4. The bot will start playing after a 3-second countdown

## Configuration

You may need to adjust the pixel coordinates in the script based on your screen resolution and game position:

- `get_pixel_colour(245, 329)` - Left side branch detection
- `get_pixel_colour(369, 327)` - Right side branch detection

To find the correct coordinates:
1. Take a screenshot while the game is running
2. Use an image editor to find the pixel coordinates
3. Update the values in the script

## Controls

- **Ctrl+C**: Stop the bot
- **Space**: Start the game (automatically pressed by the bot)

## Notes

- Make sure the game window is visible and not minimized
- The bot detects the light blue background color `(211, 247, 255)` as safe areas
- Timing is optimized for smooth gameplay with a 70ms delay between cuts

## Author

Arman Sheikhhosseini
