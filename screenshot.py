import time
import random
import pyautogui
import tkinter as tk

def screenshot():
    name = random.randint(0, 200)
    name = 'C:/Users/ardra/OneDrive/SS project/savedimage/{}.png'.format(name)
    time.sleep(3)
    img = pyautogui.screenshot(name)
    img.show()


root =tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Take Screenshot", command=screenshot)

button.pack(side=tk.LEFT)
close = tk.Button(frame, text="Close", command=quit)
close.pack(side=tk.LEFT)

root.mainloop()