
# 🔐 EncryptAndDecryptFolders

This project is a robust Python CLI tool designed to **recursively encrypt and decrypt** entire directory structures. It supports various file formats (Text, PDF, Images, Excel) and offers both local and Dockerized execution.

-----

## 📂 Project Structure

The project is organized to separate core logic from the testing environment.

```text
📦 EncryptAndDecryptFolders
 ┣ 📂 py/                  # Core logic modules
 ┃ ┣ 📜 GenKey.py          # Key generation script
 ┃ ┣ 📜 encrypt.py         # Encryption logic
 ┃ ┣ 📜 decrypt.py         # Decryption logic
 ┃ ┗ 📜 clean.py           # Cleanup utilities
 ┣ 📂 Test/                # 🧪 Comprehensive Test Environment
 ┃ ┣ 📂 img/               # Image files
 ┃ ┣ 📂 pdf/               # PDF documents
 ┃ ┣ 📂 xlxs/              # Excel spreadsheets
 ┃ ┣ 📂 English/           # Text files (English)
 ┃ ┣ 📂 Japanese/          # Text files (Japanese)
 ┃ ┗ ... (other languages)
 ┣ 📜 Dockerfile           # Docker configuration
 ┣ 📜 docker-compose.yml   # Docker Compose setup
 ┣ 📜 main.py              # Main entry point (CLI)
 ┣ 📜 requirements.txt     # Python dependencies
 ┗ 📜 LICENSE              # License information
```

-----

## 🚀 Installation & Setup

### 🐳 Option 1: Using Docker (Recommended)

Docker handles all dependencies and environment isolation.

1.  **Build and start the container:**

    ```bash
    docker-compose up -d --build
    ```

2.  **Access the container terminal:**

    ```bash
    docker exec -it EncryptAndDecryptFolders bash
    ```

### 🐍 Option 2: Local Execution

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

-----

## 💻 Usage Guide

### 1\. Generate a Security Key

Before encrypting any files, you must generate a key. This key is required to lock and unlock your data.

```bash
python main.py -g
```

*Output: A file named `FileKey.key` will be created in the root folder.*

### 2\. Encrypt a Folder

You can encrypt the included `Test` folder to verify that images, PDFs, and text files are properly secured.

```bash
# Syntax: python main.py -P {folder_path} -K {key_path} -e
python main.py -P ./Test -K FileKey.key -e
```

*After running this, try opening the PDF or Image files in the `Test` folder—they will be unreadable.*

### 3\. Decrypt a Folder

To restore your files to their original state:

```bash
# Syntax: python main.py -P {folder_path} -K {key_path} -d
python main.py -P ./Test -K FileKey.key -d
```

-----

## 📖 Command Reference

| Argument | Long Flag | Description |
| :--- | :--- | :--- |
| `-P` | `--folderPath` | Path to the target folder (e.g., `./Test`). |
| `-K` | `--keyPath` | Path to the security key file. |
| `-g` | `--genkey` | Generates a new encryption key. |
| `-e` | `--encrypt` | Activates **Encryption** mode. |
| `-d` | `--decrypt` | Activates **Decryption** mode. |
| `-h` | `--help` | Displays help message. |

-----

## ⚠️ Security Warning

> **DO NOT LOSE YOUR KEY FILE.**
>
> If you encrypt your files and lose the `.key` file, **it is mathematically impossible to recover your data**. Always keep a backup of your key in a safe location.

-----

## 📄 License

This project is open-source. For more details, please read the **[LICENSE](LICENSE)** file.