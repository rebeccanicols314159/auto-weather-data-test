import os
from datetime import datetime
import json

ORIGDIR = os.getcwd()
RTDIR = os.getcwd() + "/data_files"
os.chdir(RTDIR)

FILENAME = "data.json"
output = []

print(sorted(os.listdir()))
for i in os.listdir():
    folder = f'{RTDIR}/{i}'
    if os.path.isdir(folder):
        os.chdir(folder)
        for file in os.listdir():
            if file[-4:] == '.txt':
                record = {}
                with open(file) as f:
                    content = f.read()
                for line in content.split('\n'):
                    key,value = line.split(",")
                    if key and value:
                        record[key.strip()] = value.strip()
                record.pop('observation_time')
                record['time'] = datetime.strptime(file[13:32], "%Y-%m-%d_%H-%M-%S").isoformat()
                
                for key, value in record.copy().items():
                    try: record[key] = int(value)
                    except (KeyError, ValueError):
                        try: record[key] = float(value)
                        except (KeyError, ValueError): pass

                output.append(record)
output = sorted(output, key=lambda x: x['time'])

os.chdir(ORIGDIR)
print(json.dumps(output))
with open(FILENAME, 'w') as f:
    json.dump(output, f, indent=4)