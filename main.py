import argparse
from py.decrypt import Decrypt
from py.encrypt import Encrypt
from py.GenKey import GenKey

def main():
  parser = argparse.ArgumentParser(
    prog="encryptAnddecryptFolders",
    description="This program can encrypt and decrypt a folder."
  )

  parser.add_argument("-P","--folderPath",nargs="?", help="path to the folder you want to encrypt/decrypt")
  parser.add_argument("-K","--keyPath", nargs="?",help="path to the key")
  parser.add_argument('--decrypt','-d',action='store_true', help='Decrypt')
  parser.add_argument('--encrypt','-e',action='store_true', help='Encrypt')
  parser.add_argument('--genkey','-g',action='store_true', help='Generate key')
  

  arg = parser.parse_args()
  
  selected = sum([arg.encrypt,arg.decrypt,arg.genkey,])
  
  
  if selected > 1:
    print("Só pode escolher um")
    return
  elif selected == 0:
    print("Você precisa escolher uma opção")
    
  elif arg.genkey:
    GenKey()
  elif arg.encrypt:
    Encrypt(arg.folderPath,arg.keyPath)

  elif arg.decrypt:
    Decrypt(arg.folderPath,arg.keyPath)
    
  else:
    print("No options selected. Use -h to see the options.")
  
if __name__ == "__main__":
  main()