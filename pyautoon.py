import pyautogui

import time

time.sleep(5)
distance=400

while distance>0:
	

	pyautogui.dragRel(distance, 0, duration=0.5)   # move right
	distance=distance-50
	pyautogui.dragRel(0, distance, duration=0.5)   # move down

	pyautogui.dragRel(-distance, 0,duration=0.5)   # move left

	distance=distance-50

	pyautogui.dragRel(0, -distance, duration=0.5)   # move up