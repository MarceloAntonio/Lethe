import os
from cryptography.fernet import Fernet
from .clean import Clean
from sys import exit
from .colors import success, failure, alert, warning

warningTrigger = True

def Warning(path):
    # Asks the user for confirmation to be sure they want to encrypt the following directory
    confirm = input(f"\n{alert}Are you sure you want to encrypt the following path?\n\n {path}\n\n yes[Y] - no[N]\nOption: ")
    
    
    if confirm not in ("y", "Y"):
        print(f"\n{alert}Aborting encryption")
        exit()

def EncryptFile(file_path, fernet):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
    except PermissionError:
        print(f"{alert}Skipping protected file (read blocked): {file_path}")
        return
    except Exception as e:
        print(f"{alert}Skipping file due to error: {file_path} ({e})")
        return

    encrypted = fernet.encrypt(content)

    try:
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    except PermissionError:
        print(f"{alert}Skipping protected file (write blocked): {file_path}")
        return
    except Exception as e:
        print(f"{alert}Skipping file due to error: {file_path} ({e})")
        return

    print(f"{success} {file_path} has been encrypted")


def EncryptFolder(path,fernet):
     for files in os.listdir(path): 
        file_path = os.path.join(path, files)
        if os.path.isdir(file_path):
            print(f"\n{warning} Entering folder: {file_path}")
            EncryptFolder(file_path,fernet)
        else:
            EncryptFile(file_path,fernet)


def Encrypt(path,keyPath):
    Clean()

    # Checks if the directory exists
    if not os.path.isdir(path):
        print(f"\n{failure} Directory not found")   
        return
    
    if not os.path.exists(keyPath):
        print(f"{failure}Key was not found")
        return

    if warningTrigger == True:
        Warning(path)
    

    with open(keyPath, 'rb') as file_key:
           key = file_key.read()
                        
    fernet = Fernet(key)

    EncryptFolder(path, fernet)
             


            