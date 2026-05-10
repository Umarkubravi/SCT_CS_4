import tkinter as tk
from datetime import datetime

def key_pressed(event):
    key = event.keysym

    # Show in app
    text_box.insert(tk.END, f"{key}\n")

    # Save to file
    with open("key_logs.txt", "a") as file:
        file.write(f"{datetime.now()} - {key}\n")

root = tk.Tk()
root.title("Keyboard Activity Logger")
root.geometry("500x400")

label = tk.Label(root, text="Type inside this window")
label.pack()

text_box = tk.Text(root, height=20, width=60)
text_box.pack()

# Capture keys only in this app window
root.bind("<Key>", key_pressed)

root.mainloop()