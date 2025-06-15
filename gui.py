import streamlit as st
import os
import json
from F_I_C import save_hash, v_hashes, c_sha256

H_file = "hashes.json"

st.set_page_config(page_title="File Integrity Checker", layout="centered")
st.title("🔒 File Integrity Checker")

menu = st.radio("Choose an option:", ["Save File Hashes", "Verify File Integrity"])

# ---------------- Save File Hashes ----------------------
if menu == "Save File Hashes":
    st.write("Enter file paths manually or upload files below.")

    f_input = st.text_input("Manual file paths (comma-separated):")
    uploaded_files = st.file_uploader("Or upload files:", accept_multiple_files=True)

    if st.button("Save Hashes"):
        paths = [f.strip() for f in f_input.split(",") if f.strip()]
        temp_files = []

        # Save uploaded files temporarily
        for file in uploaded_files:
            temp_path = f"temp_{file.name}"
            with open(temp_path, "wb") as f:
                f.write(file.read())
            paths.append(temp_path)
            temp_files.append(temp_path)

        if not paths:
            st.warning("No files provided.")
        else:
            save_hash(paths)
            st.success("✅ Hashes saved successfully.")
            st.write(f"Saved to: `{H_file}`")

        # Clean up temporary files
        for temp_path in temp_files:
            if os.path.exists(temp_path):
                os.remove(temp_path)

# ---------------- Verify Hashes ----------------------
elif menu == "Verify File Integrity":
    if st.button("Verify Now"):
        if os.path.exists(H_file):
            with open(H_file, "r") as f:
                saved_hashes = json.load(f)

            st.subheader("🔎 Verifying file integrity...")
            for f_path, known_hash in saved_hashes.items():
                c_hash = c_sha256(f_path)
                st.markdown(f"**File:** `{f_path}`")

                if c_hash is None:
                    st.warning("⚠ Could not read file.")
                    continue

                if c_hash == known_hash:
                    st.success("✔ File is OK.")
                else:
                    st.error("❌ File has been changed!")
                    st.code(f"Expected: {known_hash}\nCurrent:  {c_hash}")
        else:
            st.warning("⚠ No saved hash file found. Run 'Save File Hashes' first.")
