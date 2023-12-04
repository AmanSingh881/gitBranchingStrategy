# using this program we will create a program which will save date and time in a txt file every second . after every hour a new file will be created.
import os
import time
from datetime import datetime

def create_file():
    current_time = datetime.now()
    file_name = f"data_{current_time.strftime('%Y%m%d_%H%M')}.txt"
    
    if not os.path.exists(file_name):
        with open(file_name, 'a') as file:
            file.write(f"File created at: {current_time}\n")

    return file_name

def append_random_data(file_name):
    with open(file_name, 'a') as file:
        current_time = datetime.now()
        file.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

def main():
    while True:
        current_minute = datetime.now().minute
        file_name = create_file()

        while datetime.now().minute == current_minute:
            append_random_data(file_name)
            time.sleep(1)

if __name__ == "__main__":
    main()
