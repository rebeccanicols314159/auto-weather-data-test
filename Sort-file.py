import os
import shutil
from datetime import datetime

now = datetime.now()
day = now.strftime("%Y-%m-%d")

dirname = f'{os.getcwd()}/weather-data-{day}'
print(os.getcwd())
if not os.path.exists(dirname):
    os.mkdir(dirname)

for file in os.listdir():
    if day in file:
        shutil.move(file,dirname)
        print(file,dirname)