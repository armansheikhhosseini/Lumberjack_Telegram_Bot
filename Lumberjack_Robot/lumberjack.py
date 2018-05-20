"""
Python Bot for playing lumberjack using image processing and python!
Code: Arman Sheikhhosseini
"""

import time

from pyautogui import press


def get_pixel_colour(i_x, i_y):
    import win32gui
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)


def main():
    time.sleep(3)
    press('space')
    tman = 1
    while (1 == 1):

        if (tman == 1):

            rgb = get_pixel_colour(245, 329)
            print(rgb[2])

            if rgb == (211, 247, 255):
                press('left')
                time.sleep(.07)
                continue
            else:
                press('right')
                # time.sleep(.1)
                tman = 0
                continue
        else:
            rgb = get_pixel_colour(369, 327)
            print(rgb[2])

            if rgb == (211, 247, 255):
                press('right')
                time.sleep(.07)
                continue
            else:
                press('left')
                # time.sleep(.1)
                tman = 1
                continue


if __name__ == '__main__':
    main()
