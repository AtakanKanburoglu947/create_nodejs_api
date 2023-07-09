import os
def create_config_folder():
    config_directory = os.path.join(os.getcwd(), "config")
    os.mkdir(config_directory)
    return config_directory
