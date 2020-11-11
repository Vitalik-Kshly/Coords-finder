import pyautogui
import tkinter
import ctypes


def printCoords():
    coords.insert(0, pyautogui.position())

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
root = tkinter.Tk()
coords = tkinter.Listbox(root,height = 1, width=10)
coords.pack(side = "left")
while 1:
    printCoords()
    root.update()
