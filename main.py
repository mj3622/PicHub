import tkinter as tk
from config_ui import show_config_ui
from upload_ui import upload_image
from init import gene_repo
import webbrowser

def open_webpage(event):
    webbrowser.open("https://github.com/mj3622/PicHub")

root = tk.Tk()
root.title("PicHub")

window_width = 600
window_height = 150

root.geometry(f"{window_width}x{window_height}+{root.winfo_screenwidth() // 2 - window_width // 2}+{root.winfo_screenheight() // 2 - window_height // 2}")

root.resizable(width=False, height=False)

button_frame = tk.Frame(root)
button_frame.pack(pady=30)

upload_button = tk.Button(button_frame, text="upload", command=lambda:upload_image(root),width=15,height=2)
config_button = tk.Button(button_frame, text="config", command=lambda:show_config_ui(root), width=15, height=2)
init_button = tk.Button(button_frame, text="init", command=gene_repo, width=15, height=2)

init_button.grid(row=0, column=0, padx=10)
upload_button.grid(row=0, column=1, padx=10)
config_button.grid(row=0, column=2, padx=10)


link = tk.Label(root, text="Document", fg="blue", cursor="hand2")

link.bind("<Button-1>", open_webpage)

link.pack()

root.mainloop()
