from sys import executable
from subprocess import check_call
import os
import sqlite3


def install() -> None:
    # Takes the list of modules to be installed from requirements.txt and installs them
    check_call([executable, "-m", "pip", "install", "-r", "requirements.txt"])
    create_dirs()
    
    return
    
    
def create_dirs() -> None:
    
    # Create the "assets/history" directories if they do not exist
    print("Creating save directories.")
    os.makedirs("assets/history", exist_ok=True)
    print("assets/history done.")
    os.makedirs("assets/images", exist_ok=True)
    print("assets/images done.")
    
    if not os.path.exists("assets/history/history.db"):
        
        print("Creating sqlite database.")
        open(r"assets\history\history.db", "w")

        history = sqlite3.connect(r"assets\history\history.db")
        cursor = history.cursor()
        cursor.execute("CREATE TABLE history (\n\tactions_id INTEGER NOT NULL,\n\tJSON TEXT NOT NULL,\n\tPRIMARY KEY (actions_id)\n)")
        
        history.commit()
        history.close()
        print("Sqlite database created successfully.")

    print("creating json file.")
    with open(r"assets\history\history.json", "w") as f:
        f.write("[]")
        print("json file created successfully.")

if __name__ == "__main__":
    install()

# recommended to run this file if it is the first time running the program
