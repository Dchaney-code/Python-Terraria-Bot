import pydirectinput
import time
# Give's the user 10 seconds to switch to the Terraria window
print("Starting Auto_swinger in 10 seconds switch to Terraria now.")
time.sleep(10)
print("Starting the loop! Press Ctrl+C in the terminal to stop.")
# Loop's the code below infintely
while True:
# Automatically right clicks
    pydirectinput.mouseDown()
    time.sleep(0.1)
    pydirectinput.mouseUp()
    print("Swung sword...")
# Waits a second till the loop restarts
    time.sleep(1)