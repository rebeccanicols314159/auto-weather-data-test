import os
import shutil
from datetime import datetime

now = datetime.now()
day = now.strftime("%Y-%m-%d")

def get_folder_name():
    dirname = f'{os.getcwd()}/data_files/weather_data_{day}'
    print(os.getcwd())
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    return dirname

def sort_files():
    dname = get_folder_name()
    for file in os.listdir():
        if day in file:
            shutil.move(file,dname)
            print(file,dname)