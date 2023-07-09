import os
from pathlib import Path

def create_api_folder():
    current_directory = Path.cwd()
    api_directory = current_directory / "api"
    api_directory.mkdir()

    subdirectories = ["controllers", "helpers", "middlewares", "models",
                      "routes", "services", "validations"]

    for subdir in subdirectories:
        (api_directory / subdir).mkdir()

    os.chdir(api_directory)
