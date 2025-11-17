import os
from cryptography.fernet import Fernet, InvalidToken
from .clean import Clean


def DecryptFile(file_path, fernet):
    try:
        with open(file_path, "rb") as encrypted_file:
                        encrypted_data = encrypted_file.read()
                            
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_path, "wb") as decrypted_file:
                        decrypted_file.write(decrypted_data)

        print(f"\n{file_path} has been decrypted")
    except InvalidToken:
            print(f"\nThe file {file_path} has already been decrypted.")

def DecryptFolder(path,fernet):
    for files in os.listdir(path):
        file_path = os.path.join(path,files)
        if os.path.isdir(file_path):
            print(f"\nEntering folder: {file_path}")
            DecryptFolder(file_path,fernet)
        else:
            DecryptFile(file_path,fernet)



# Function to decrypt files
def Decrypt(path,keyPath):
    Clean()

    # Checks if the directory exists
    if not os.path.isdir(path):
        print("\nDirectory not found")   
        return
    if not os.path.exists(keyPath):
        print("Key was not found")
        return


    with open(keyPath, "rb") as file_key:
        key = file_key.read()
                            
    fernet = Fernet(key)

    DecryptFolder(path, fernet)


    