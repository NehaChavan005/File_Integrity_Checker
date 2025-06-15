# File_Integrity_Checker
File Integrity Checker – A Python-based tool (CLI + GUI) to calculate and verify SHA-256 hashes for files, ensuring their integrity and detecting unauthorized changes. Includes a Streamlit web interface.

# 🔒 File Integrity Checker

This project is a simple and effective File Integrity Checker built in Python. It provides both a **command-line interface (CLI)** and an intuitive **Streamlit-based GUI** for:

- Generating and saving SHA-256 hashes of files
- Verifying whether files have been altered since the last hash was saved

## 🚀 Features

- 🧮 Uses SHA-256 to ensure strong cryptographic file checks
- 💾 Saves hashes in a JSON file (`hashes.json`)
- 🕵️‍♂️ Verifies file integrity against saved hashes
- 🌐 User-friendly GUI using Streamlit
- 🧰 Lightweight and easy to run locally

## 🗂 Files

- `F_I_C.py` — CLI tool to save and verify file hashes.
- `gui.py` — Streamlit web app for hash saving and integrity checking.

## 📦 Requirements

- Python 3.x
- `streamlit` (for GUI)

Install dependencies:

```bash
pip install streamlit

1. Run CLI version
python F_I_C.py

2. Run GUI version
streamlit run gui.py

📁 Output
All saved hashes are stored in:
hashes.json

🔐 Why Hashing?
Using SHA-256 helps ensure that files haven't been tampered with. Even a tiny change in file contents produces a completely different hash.




