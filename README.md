# CryptoClippy

CryptoClippy is a proof-of-concept (PoC) cryptocurrency clipper.
It is designed as a security research and educational tool to demonstrate how clipboard-based address swapping attacks could be carried out, and to help raise awareness of these risks.

⚠️ Disclaimer
This project is provided strictly for educational, awareness, and testing purposes only.
It does not contain or encourage malicious functionality beyond demonstration.
The author does not condone misuse of this code, and takes no responsibility for how others may use it.
---

## Features

* Monitors the clipboard for copied cryptocurrency wallet addresses
* Replaces detected addresses with predefined attacker-controlled addresses (PoC behavior)
* Adds itself to **startup locations** to ensure persistence
* Demonstrates multiple persistence methods (registry keys, startup folder, scheduled tasks, etc.)
* Lightweight and runs silently in the background

---

## Supported Coins

The PoC is configured to recognize and target wallet addresses for:

* **Bitcoin (BTC)**
* **Ethereum (ETH)**
* **Litecoin (LTC)**
* **Monero (XMR)**
* **Ripple (XRP)**
* **Dogecoin (DOGE)**
* Other common cryptocurrency formats can be added as needed

---

## Purpose

* Highlight the **security risks** of blindly copy-pasting wallet addresses
* Demonstrate how malware achieves **persistence** through multiple startup mechanisms
* Provide a base for **research and security testing**
* Encourage users and organizations to adopt stronger defenses against clipboard-based attacks

---

## Usage

1. Clone the repository

   ```bash
   git clone https://github.com/r3ci/CryptoClippy.git
   cd CryptoClippy
   ```
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Run the script (for demonstration purposes)

   ```bash
   python build.py
   ```

---

## Ethical & Legal Notice

* This project is a **non-malicious PoC**.
* It is intended for **educational demonstrations, penetration testing labs, and awareness training**.
* Using software like this for unauthorized interception or tampering with cryptocurrency transactions is **illegal** and unethical.
* Always use responsibly in **controlled environments**.