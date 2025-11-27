from cryptography.fernet import Fernet
import os
from .colors import success

def GenKey():
    key = Fernet.generate_key()
    
    base_name = "FileKey"
    extension = ".key"
    final_name = base_name + extension
    
    count = 0
    
    # Enquanto o arquivo existir, incrementa o contador e tenta novo nome
    while os.path.exists(final_name):
        count += 1
        final_name = f"{base_name}{count}{extension}"
    
    # Agora salvamos com o final_name que garantimos ser único
    with open(final_name, 'wb') as filekey:
        filekey.write(key)
        
    fullPath = os.path.abspath(final_name)
    print(f"\n{success} The key was created successfully: {fullPath}\n")

if __name__ == "__main__":
    GenKey()