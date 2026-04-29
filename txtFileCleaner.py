import os

os.chdir(f'{os.getcwd()}/data_files')
rtdir = os.getcwd()
folders = os.listdir()
for i in folders.copy():
    if not "weather_data" in i:
        folders.remove(i)

def change_txt_files(fders):
    for folder in fders:
        os.chdir(f'{rtdir}/{folder}')
        for file in os.listdir():
            if 'weather-data' in file:
                with open(file, 'r') as f:
                    content = f.read()
                # Replace spaces with commas
                new_content = content.replace(' ', ',')
                # Fix 'x,PM' or 'x,AM' to 'x PM' or 'x AM'
                for i in range(len(new_content)):
                    if new_content[i] == 'P' or new_content[i] == 'A' and new_content[i+1] == 'M':
                        if new_content[i-1] == ',':
                            new_content = new_content[:i-1] + ' ' + new_content[i:]
                with open(file, 'w') as f:
                    f.write(new_content)

change_txt_files(folders)