import sys
from github import Github
from configparser import ConfigParser
import uuid
import os

def upload_image(image_path):
    config = ConfigParser()
    config_file = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.ini'))
    config.read(config_file)

    GITHUB_TOKEN = config.get('Settings', 'token', fallback='')
    REPO_NAME = config.get('Settings', 'repository_name', fallback='')
    BRANCH_NAME = config.get('Settings', 'branch_name', fallback='')

    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)

    new_filename = f'{uuid.uuid4()}{os.path.splitext(image_path)[1]}'
    with open(image_path, 'rb') as file:
        content = file.read()
    
    repo.create_file(f'images/{new_filename}', 'Upload image from ', content, branch=BRANCH_NAME)
    
    return f'https://raw.githubusercontent.com/{REPO_NAME}/{BRANCH_NAME}/images/{new_filename}'


if __name__ == "__main__":
    res = 'Upload Success:\n'
    for i in range(1, len(sys.argv)):
        image_path = sys.argv[i]
        url = upload_image(image_path)
        if url:
            res += f'{url}\n'
        else:
            res += f'Failed\n'

    res = res[:-1]
    print(res)

