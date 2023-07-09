import subprocess
def install_packages():
    packages = [
        ["npm", "init", "-y"],
        ["npm", "install", "express"],
        ["npm", "install", "dotenv"],
        ["npm", "install", "mysql2"],
        ["npm", "install", "--save-dev", "nodemon"],
        ["npm", "install", "axios"]
    ]

    for package in packages:
        try:
            subprocess.run(package, shell=True)
        except subprocess.CalledProcessError as exception:
            raise Exception(f"Error installing package '{package[-1]}': {exception}")
