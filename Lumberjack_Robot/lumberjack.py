"""
Python Bot for playing lumberjack using image processing and PyAutoGUI!
This script automatically plays the Lumberjack game in Telegram by detecting
pixel colors and simulating keyboard inputs.

Author: Arman Sheikhhosseini
Requirements: pyautogui, win32gui (Windows only)

Usage:
1. Open the Lumberjack game in your browser or Telegram
2. Run this script
3. The bot will start playing after a 3-second delay

Note: You may need to adjust the pixel coordinates (245, 329) and (369, 327)
based on your screen resolution and game position.
"""

import time
from pyautogui import press


def get_pixel_colour(x, y):
    """
    Get the RGB color of a pixel at the specified coordinates.
    
    Args:
        x (int): X coordinate
        y (int): Y coordinate
        
    Returns:
        tuple: RGB color values (r, g, b)
    """
    import win32gui
    desktop_window_id = win32gui.GetDesktopWindow()
    desktop_window_dc = win32gui.GetWindowDC(desktop_window_id)
    long_colour = win32gui.GetPixel(desktop_window_dc, x, y)
    colour = int(long_colour)
    return (colour & 0xff), ((colour >> 8) & 0xff), ((colour >> 16) & 0xff)


def main():
    """
    Main game loop that plays the Lumberjack game automatically.
    """
    print("Starting Lumberjack Bot in 3 seconds...")
    print("Make sure the game window is visible and positioned correctly!")
    time.sleep(3)
    
    # Start the game
    press('space')
    print("Game started! Bot is now playing...")
    
    # Track which side the man is on (1 = left, 0 = right)
    man_position = 1
    
    # Target color for safe area (light blue background)
    target_color = (211, 247, 255)
    
    try:
        while True:
            if man_position == 1:  # Man is on the left side
                # Check pixel on the left side for branch
                rgb = get_pixel_colour(245, 329)
                print(f"Left side RGB: {rgb}, Blue component: {rgb[2]}")
                
                if rgb == target_color:
                    # Safe to cut on the left, move to right
                    press('left')
                    time.sleep(0.07)
                else:
                    # Branch detected on left, move to right side
                    press('right')
                    man_position = 0
                    
            else:  # Man is on the right side
                # Check pixel on the right side for branch
                rgb = get_pixel_colour(369, 327)
                print(f"Right side RGB: {rgb}, Blue component: {rgb[2]}")
                
                if rgb == target_color:
                    # Safe to cut on the right, move to left
                    press('right')
                    time.sleep(0.07)
                else:
                    # Branch detected on right, move to left side
                    press('left')
                    man_position = 1
                    
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("Make sure the game window is visible and try again.")


if __name__ == '__main__':
    main()
