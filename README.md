<div align="center">

# 🔗 CryptoClippy

**CryptoClippy** is a **proof-of-concept (PoC)** cryptocurrency clipper.  
It is designed as a **security research and educational tool** to demonstrate how clipboard-based address swapping attacks could be carried out, and to help raise awareness of these risks.  

</div>

---

## ✨ Features

- 📋 Demonstrates monitoring the clipboard for copied cryptocurrency wallet addresses  
- 🔄 Simulates replacement of detected addresses with predefined PoC values  
- ⚙️ Explains common persistence methods (startup folder, registry keys, scheduled tasks, etc.)  
- 🪶 Lightweight and runs silently in the background  

---

## 💰 Supported Coins

This PoC can be configured to recognize wallet address formats for:

- **Bitcoin (BTC)**  
- **Ethereum (ETH)**  
- **Litecoin (LTC)**  
- **Monero (XMR)**  
- **Ripple (XRP)**  
- **Dogecoin (DOGE)**  
- Other common cryptocurrency formats can be added for demonstration  

---

## 🎯 Purpose

- 🔐 Highlight the **security risks** of blindly copy-pasting wallet addresses  
- 🛠️ Demonstrate how malware could achieve **persistence** through multiple startup mechanisms  
- 🧪 Provide a base for **research and testing in controlled environments**  
- 🛡️ Encourage users and organizations to adopt stronger defenses  

---

## 🚀 Usage

```bash
# Clone the repository
git clone https://github.com/r3ci/CryptoClippy.git
cd CryptoClippy

# Install dependencies
pip install -r requirements.txt

# Run (PoC only)
python build.py
````

---

<div align="center">

### ⚖️ Ethical & Legal Notice 
</div>
🔸 This repository is a **non-malicious PoC** created solely for **research, education, and awareness**.  
🔸 It does **not encourage or support malicious activity**.  
🔸 Using software like this to intercept or tamper with cryptocurrency transactions without consent is **illegal** and unethical.  
🔸 Always use responsibly in **controlled environments** such as penetration testing labs or awareness training.   