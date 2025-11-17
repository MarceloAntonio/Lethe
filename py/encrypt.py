import os
from cryptography.fernet import Fernet
from .clean import Clean


def EncryptFile(file_path, fernet):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
    except PermissionError:
        print(f"Skipping protected file (read blocked): {file_path}")
        return
    except Exception as e:
        print(f"Skipping file due to error: {file_path} ({e})")
        return

    encrypted = fernet.encrypt(content)

    try:
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    except PermissionError:
        print(f"Skipping protected file (write blocked): {file_path}")
        return
    except Exception as e:
        print(f"Skipping file due to error: {file_path} ({e})")
        return

    print(f"\n{file_path} has been encrypted\n")


def EncryptFolder(path,fernet):
     for files in os.listdir(path): 
        file_path = os.path.join(path, files)
        if os.path.isdir(file_path):
            print(f"\nEntering folder: {file_path}")
            EncryptFolder(file_path,fernet)
        else:
            EncryptFile(file_path,fernet)


def Encrypt(path,keyPath):
    Clean()

    # Checks if the directory exists
    if not os.path.isdir(path):
        print("\nDirectory not found")   
        return
    
    if not os.path.exists(keyPath):
        print("Key was not found")
        return

    # Asks the user for confirmation to be sure they want to encrypt the following directory
    confirm = input(f"\nAre you sure you want to encrypt the following path?\n\n {path}\n\n yes[Y] - no[N]\nOption: ")
    
    
    if confirm not in ("y", "Y"):
        print("\nAborting encryption")
        return
    

    with open(keyPath, 'rb') as file_key:
           key = file_key.read()
                        
    fernet = Fernet(key)

    EncryptFolder(path, fernet)
             


            