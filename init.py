from github import Github
import tkinter as tk
from configparser import ConfigParser

def gene_repo():
    config = ConfigParser()
    config.read('config.ini')
    access_token = config.get('Settings', 'token', fallback='')
    repo_name = config.get('Settings', 'repository_name', fallback='').split('/')[-1]

    if not access_token or not repo_name:
        tk.messagebox.showwarning("Configuration Required", "Please configure your settings first.")
        return

    g = Github(access_token)

    repo_description = "This is a repository for storing images uploaded by PicHub."

    user = g.get_user()

    try:
        repo = user.get_repo(repo_name)
        tk.messagebox.showwarning("Repository Exists", f"Repository '{repo.full_name}' already exists.")
    except Exception as e:
        repo = user.create_repo(name=repo_name, description=repo_description, auto_init=True)

        tk.messagebox.showinfo("Repository Created", f"Repository '{repo.full_name}' created successfully.")