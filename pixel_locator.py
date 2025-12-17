import pyautogui
import time

def locate_health_bar():
    print("Please position the mouse over the health bar.")
    print("you have five seconds to position it in the correct location.")
    time.sleep(5)

    x, y = pyautogui.position()

    pixel_colour = pyautogui.screenshot().getpixel((x, y))

    print(f"Coordinates: {x}, {y}")
    print(f"Colour detected: {pixel_colour}")

    if pixel_colour[0] > 150 and pixel_colour[1] < 50:
        print("--- Verified health location ---")
    else:
        print("--- ERROR cannot locate health (make sure your cursor is in the correct location)")
if __name__ == "__main__":
    locate_health_bar()