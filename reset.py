from sys import executable
from subprocess import check_call

import sqlite3


def clear_all():

    print("Cleaning database .")

    # Connects to the database
    history = sqlite3.connect(r"assets\database\history.db")

    # Sets cursor
    cursor = history.cursor()
    
    try:
        
        # Gets ready to save it to database
        cursor.execute("DELETE FROM history")
    
        # Saves it to database
        history.commit()
        
    except sqlite3.OperationalError:
        
        # if table not found create table
        cursor.execute("CREATE TABLE history (\n\tactions_id INTEGER NOT NULL,\n\tJSON TEXT NOT NULL,\n\tPRIMARY KEY (actions_id)\n)")
        
        # Saves table
        history.commit()
    
    # Terminates connection
    history.close()

    print("Database cleared.")

    # To delete all __pycache__
    check_call([executable, "-m", "pyclean", "."])

    print("Clearing Json .")

    # to clear Json history
    with open(r"assets\json\history.json", "w") as json:
        json.write("[]")
    
    print("Json history cleared.")
    
    # to clear images history
    with open(r"assets\images\images.png", "w"):
        pass
    
    print("Image file cleared.")


if __name__ == "__main__":
    clear_all()
