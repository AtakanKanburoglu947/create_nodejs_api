import os
from api import create_api_folder
from env import create_env_file
from packages import install_packages
from config import create_config_folder
from app import create_app
def create_nodejs_api(project_name):
    try:
        new_directory = os.path.join(os.getcwd(), project_name)
        os.mkdir(new_directory)
        print(f"Folder '{project_name}' created.")
        os.chdir(new_directory)
        install_packages()
        create_api_folder()
        create_config_folder()
        create_env_file()
        create_app()
        print("Node.js API created successfully.")
    except Exception as exception:
        print("An error occurred:", str(exception))
project_name = "nodejs_api"
create_nodejs_api(project_name)
