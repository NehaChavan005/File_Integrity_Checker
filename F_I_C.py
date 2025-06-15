import hashlib
import os
import json


#H_file is a constant variable
#hashes.json is a relative path of files to READ or WRITE
H_file = "hashes.json"


#------------Calculate SHA-256 hash of a file--------------------------

#hashlib >>>>> is module in python which creates fixed-size cryptographic hashes
#hashlib.sha256(file_data) >>>>> creates a SHA-256 hash object for the input data
#.hexdigest() >>>>> converts the hash into a readable hexadecimal string

#e >>>>> variable od exception and gives actual error message from the exception

def c_sha256(f_path):
    try:
        with open(f_path, "rb") as  f:
            f_data = f.read()
        return hashlib.sha256(f_data).hexdigest()
    except Exception as e:
        print(f"Errors with {f_path}: {e}")
        return None
    

#--------------------Function to save hashes of multiple files------------------------------------

#hashes >>>>> This dictionary will store filename-to-hash mappings: {filename: sha256_hash}
#f_path >>>>> Loop for each file path in the list, call c_sha256(f_path) — presumably a function that returns the SHA-256 hash of the file contents or None if it fails.
#hash is valid (if f_hash): >>>>> Store the hash in the dictionary under the key f_path, Print confirmation: "Hash saved for: <filename>"
#Write the hashes dictionary into this file in JSON format, pretty-printed with indentation.
#Print a final confirmation that all hashes have been saved.

def save_hash(f_list):
    hashes = {}
    for f_path in f_list:
        f_hash = c_sha256(f_path)
        if f_hash:
            hashes[f_path] = f_hash
            print(f"Hash saved for: {f_path}")
    with open(H_file, "w") as f:
        json.dump(hashes, f, indent=4)
    print(f"\n All hashes saved to '{H_file}'.")



#--------------------------Function to verify hashes of files later------------------------------------------------

def v_hashes():
    try:
        with open(H_file, "r") as f:
            saved_hashes = json.load(f) # Load saved hashes from file
    except FileNotFoundError:
        print("No saved hash file found. Run Save mode first.")
        return # Stop if no hash file exists-------------------------If the file doesn't exist, it informs the user and stops.
    

    print("\n Verifying file integrity... ")
    for f_path, known_hash in saved_hashes.items():
        c_hash = c_sha256(f_path) # Compute current hash of the file
        if c_hash is None: 
            continue # Skip if hash calculation failed --------------------------If c_sha256 returns None (maybe the file is missing or unreadable), it skips that file.
        #Otherwise, it compares the current hash with the saved one.
        print(f"\n File: {f_path}")
        if c_hash == known_hash:
            print("File is OK.") # Hash matches saved hash
        else:
            print("WARNING: File has been changed!") # Hash mismatch
            print(f"Expected: {known_hash}")
            print(f"Current: {c_hash}")



#----------------------------Main Menu----------------------------------------------------------

def main():
    print("FILE INTEGRITY CHECKER")
    print("------------------------")
    print("1) Save file hashes ")
    print("2) Verify file integrity")
    choice = input("Choose an option (1/2): ").strip()

    if choice == '1':
        print("\nEnter file path separated by commas (e.g. file1.txt, file2.jpg):")
        f_input = input("Files: ").strip()
        f_list = [f.strip() for f in f_input.split(',')]
        save_hash(f_list)
    elif choice == '2':
        v_hashes()
    else:
        print("Invalid option. Please enter 1 or 2.")


#-----------Run Program----------------------

if __name__ == "__main__":
    main()

    