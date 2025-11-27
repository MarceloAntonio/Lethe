import argparse
from py.decrypt import Decrypt
import py.encrypt
from py.encrypt import Encrypt
from py.GenKey import GenKey


def main():
  parser = argparse.ArgumentParser(
    prog="lethe.py",
    description="This project is a robust Python CLI tool designed to recursively encrypt and decrypt entire directory structures. It supports various file formats (Text, PDF, Images, Excel)"
  )

  parser.add_argument("-P","--folderPath",nargs="?", help="Path to the target folder (e.g., ./Test).")
  parser.add_argument("-K","--keyPath", nargs="?",help="Path to the security key file.")
  parser.add_argument('--decrypt','-d',action='store_true', help='Activates Decryption mode.')
  parser.add_argument('--encrypt','-e',action='store_true', help='Activates Encryption mode.')
  parser.add_argument('--genkey','-g',action='store_true', help='Generates a new encryption key.')
  parser.add_argument('--skip','-s',action='store_true', help='	Skips the warning confirmation prompt.')
  

  arg = parser.parse_args()
  
  selected = sum([arg.encrypt,arg.decrypt,arg.genkey,])

  if arg.skip:
    py.encrypt.warningTrigger = False

  if selected > 1:
    print("Only one action option can be selected at a time. Try using only -e or -d.")
    return
    
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