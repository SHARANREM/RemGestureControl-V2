import pyautogui
from datetime import datetime
import os

folder = "screenshots"
os.makedirs(folder, exist_ok=True)

filename = datetime.now().strftime("%Y%m%d_%H%M%S.png")
path = os.path.join(folder, filename)

screenshot = pyautogui.screenshot()
screenshot.save(path)

print(f"Screenshot saved: {path}")