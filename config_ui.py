import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Entry, Button
from configparser import ConfigParser


def show_config_ui(root):
    config_window = Toplevel(root)
    config_window.title("User Configuration")

    root.update_idletasks()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_x()
    root_y = root.winfo_y()

    config_window.update_idletasks()
    config_window_width = 600
    config_window_height = 200
    
    position_right = int(root_x + (root_width - config_window_width) / 2)
    position_down = int(root_y + (root_height - config_window_height) / 2)
    
    config_window.geometry(f"{config_window_width}x{config_window_height}+{position_right}+{position_down}")
    
    config = ConfigParser()
    config.read('config.ini')
    
    token = config.get('Settings', 'token', fallback="")
    repository_name = config.get('Settings', 'repository_name', fallback="")
    branch_name = config.get('Settings', 'branch_name', fallback="")
    
    Label(config_window, text="Token").grid(row=0, column=0, padx=10, pady=10)
    token_entry = Entry(config_window, width=40)
    token_entry.grid(row=0, column=1, padx=10, pady=10)
    token_entry.insert(0, token)


    Label(config_window, text="Repository").grid(row=1, column=0, padx=10, pady=10)
    repo_entry = Entry(config_window, width=40)
    repo_entry.grid(row=1, column=1, padx=10, pady=10)
    repo_entry.insert(0, repository_name)


    Label(config_window, text="Branch").grid(row=2, column=0, padx=10, pady=10)
    branch_entry = Entry(config_window, width=40)
    branch_entry.grid(row=2, column=1, padx=10, pady=10)
    branch_entry.insert(0, branch_name)
 
    
    def save_config():
        config.set('Settings', 'token', token_entry.get())
        config.set('Settings', 'repository_name', repo_entry.get())
        config.set('Settings', 'branch_name', branch_entry.get())
        
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        
        messagebox.showinfo("Saved", "Configuration has been saved.")
        config_window.destroy()
    
    Button(config_window, text="Save", command=save_config).grid(row=3, column=1, columnspan=2, pady=10)
    
