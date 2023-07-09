import subprocess
def install_packages():
    packages = [
        ["npm", "init", "-y"],
        ["npm", "install", "express"],
        ["npm", "install", "dotenv"],
        ["npm","install","mongodb"],
        ["npm","install","mongoose"],
        ["npm","install","sqlite3"],
        ["npm", "install", "mysql2"],
        ["npm", "install", "--save-dev", "nodemon"],
        ["npm", "install", "axios"]
    ]
    for package in packages[0:3]:
        try:
            subprocess.run(package, shell=True)
        except subprocess.CalledProcessError as exception:
            raise Exception(f"Error installing package '{package[-1]}': {exception}")
    print("Database? (1: MySql, 2: MongoDb, 3: SqLite)")
    database = int(input())
    if(database==1):
        subprocess.run(packages[6],shell=True)
    elif(database==2):
        subprocess.run(packages[3],shell=True)
        subprocess.run(packages[4],shell=True)
    elif(database==3):
        subprocess.run(packages[5],shell=True)
    else: 
        print("Skipped database")
    print("Install Axios? (Y/N)")
    axios = str(input().lower())
    if(axios=="y"):
        subprocess.run(packages[8],shell=True)
    else:
        print("Skipped installing Axios")
    print("Install Nodemon? (Y/N)")
    nodemon = str(input().lower())
    if(nodemon == "y"):
        subprocess.run(packages[7],shell=True)
    else:
        print("Skipped installing Nodemon")



        
