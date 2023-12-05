import json,random
import time
import os, pytz
from datetime import datetime, timedelta

DATA_DIR = "/home/ispock/Desktop/data/"  
ist =  pytz.timezone('Asia/Kolkata')
def create_new_file(key):
    ist_offset = timedelta(hours=5, minutes=30)
    utc_time = datetime.utcnow()
    ist_time = utc_time + ist_offset
    file_name = str(ist_time.strftime("%Y%m%d_%H%M")) 
    file_path = os.path.join(key, file_name)
    return file_path


def append_data_to_json_file(data, file_path):
    try:
        with open(file_path+'.json', "a") as file:
            json.dump(data, file)
            file.write("\n")
    except Exception as e:
        print(f"2 Error occurred in appending data in the file : {e}")



def start_server():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    while True:
            current_minute = None
            current_file = None
            
            while True:
                try:       
                    data_dict = {"aman":[int(time.time()*1000),random.randint(1,100)]*10}
                    timestamp = datetime.now(ist)
                    
                    for key in data_dict:
                        pass

                    path1 = DATA_DIR+key
                    if not os.path.exists(path1):
                        os.makedirs(path1)

                    if current_minute != timestamp.minute:
                        current_minute = timestamp.minute
                        current_file = create_new_file(path1)
                    # print(data_dict)
                    append_data_to_json_file(data_dict, current_file)

                except Exception as e:
                    print(f"An exception occured : {e}, {time.time()}")
                time.sleep(1)

if __name__ == "__main__":
    start_server()