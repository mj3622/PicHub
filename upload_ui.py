import os
import uuid
from github import Github
import tkinter as tk
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
import webbrowser
from configparser import ConfigParser
import github.GithubException

def select_image():
    Tk().withdraw() 
    filename = askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
    return filename

def upload_to_github(file_path, repo, branch='master'):
    new_filename = f'{uuid.uuid4()}{os.path.splitext(file_path)[1]}'
    with open(file_path, 'rb') as file:
        content = file.read()
    
    repo.create_file(f'images/{new_filename}', 'Upload image from ', content, branch=branch)
    return new_filename

def upload_image(root):
    config = ConfigParser()
    config.read('config.ini')

    GITHUB_TOKEN = config.get('Settings', 'token', fallback='')
    REPO_NAME = config.get('Settings', 'repository_name', fallback='')
    BRANCH_NAME = config.get('Settings', 'branch_name', fallback='')

    if not GITHUB_TOKEN or not REPO_NAME or not BRANCH_NAME:
        messagebox.showwarning("Configuration Required", "Please configure your settings first.")
        return

    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while connecting to GitHub: {e}")
        return
    
    image_path = select_image()
    if not image_path:
        messagebox.showwarning("No File Selected", "No file selected.")
        return
    
    try:
        filename = upload_to_github(image_path, repo, BRANCH_NAME)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while uploading the image: {e}")
        return

    file_url = f'https://raw.githubusercontent.com/{REPO_NAME}/{BRANCH_NAME}/images/{filename}'
    print(f'Image uploaded successfully: {file_url}')

    tk.messagebox.showinfo("Uploaded", "Image uploaded successfully,the link has been copied to the clipboard.")
    root.clipboard_clear()
    root.clipboard_append(file_url)
    
    webbrowser.open_new_tab(file_url)


