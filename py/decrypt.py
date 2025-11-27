import os
from cryptography.fernet import Fernet, InvalidToken
from .clean import Clean
from .colors import failure, success, alert, warning


def DecryptFile(file_path, fernet):
    try:
        with open(file_path, "rb") as encrypted_file:
                        encrypted_data = encrypted_file.read()
                            
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_path, "wb") as decrypted_file:
                        decrypted_file.write(decrypted_data)

        print(f"{success} {file_path} has been decrypted")
    except InvalidToken:
            print(f"{alert} The file {file_path} has already been decrypted.")

def DecryptFolder(path,fernet):
    for files in os.listdir(path):
        file_path = os.path.join(path,files)
        if os.path.isdir(file_path):
            print(f"{warning} Entering folder: {file_path}")
            DecryptFolder(file_path,fernet)
        else:
            DecryptFile(file_path,fernet)



# Function to decrypt files
def Decrypt(path,keyPath):
    Clean()

    # Checks if the directory exists
    if not os.path.isdir(path):
        print(f"\n{failure}Directory not found")   
        return
    if not os.path.exists(keyPath):
        print(f"\n{failure}Key was not found")
        return


    with open(keyPath, "rb") as file_key:
        key = file_key.read()
                            
    fernet = Fernet(key)

    DecryptFolder(path, fernet)


    