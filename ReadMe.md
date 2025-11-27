<div align="center"> <img src="assets/RiverLethe.png" width="70%" alt="Lethe Logo"/> <h1>Lethe</h1>

<p> <b>The river of forgetfulness.</b> </p>

<a href="https://www.python.org/"> <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version"/> </a> <a href="https://docker.com"> <img src="https://img.shields.io/badge/Docker-Ready-2496ED.svg" alt="Docker"/> </a> <a href="LICENSE"> <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"/> </a>



</div>


Named after the river in Greek mythology whose waters caused souls to lose all memory of their past lives, **Lethe** is a tool designed to make your data "forgotten" to unauthorized eyes.

This project is a robust Python CLI tool designed to **recursively encrypt and decrypt** entire directory structures. It supports various file formats (Text, PDF, Images, Excel) and offers both local and Dockerized execution.

## Installation & Setup

### Option 1: Using Docker

Docker handles all dependencies and environment isolation.

1.  **Build and start the container:**

    ```bash
    docker-compose up -d --build
    ```

2.  **Access the container terminal:**

    ```bash
    docker exec -it lethe bash
    ```

### Option 2: Local Execution

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage Guide

### 1. Generate a Security Key

Before encrypting any files, you must generate a key. This key is required to lock and unlock your data.

```bash
python lethe.py -g
````

*Output: A file named `FileKey.key` will be created in the root folder.*

### 2\. Encrypt a Folder

You can encrypt the included `Test` folder to verify that images, PDFs, and text files are properly secured.

```bash
# Syntax: python lethe.py -P {folder_path} -K {key_path} -e
python lethe.py -P ./Test -K FileKey.key -e
```

*After running this, try opening the PDF or Image files in the `Test` folder—they will be unreadable.*

### 3\. Decrypt a Folder

To restore your files to their original state:

```bash
# Syntax: python lethe.py -P {folder_path} -K {key_path} -d
python lethe.py -P ./Test -K FileKey.key -d
```

### 4\. Skip Warning (Optional)

If you want to run the script without confirming the warning prompt (useful for automation), use the `-s` flag:

```bash
python lethe.py -P ./Test -K FileKey.key -e -s
```

-----

## Command Reference

| Argument | Long Flag      | Description                                      |
| :------- | :------------- | :----------------------------------------------- |
| `-P`     | `--folderPath` | Path to the target folder (e.g., `./Test`).      |
| `-K`     | `--keyPath`    | Path to the security key file.                   |
| `-g`     | `--genkey`     | Generates a new encryption key.                  |
| `-e`     | `--encrypt`    | Activates **Encryption** mode.                   |
| `-d`     | `--decrypt`    | Activates **Decryption** mode.                   |
| `-s`     | `--skip`       | Skips the warning confirmation prompt.           |
| `-h`     | `--help`       | Displays help message.                           |

-----

## Security Warning

> **DO NOT DRINK FROM THE WRONG WATERS (DO NOT LOSE YOUR KEY).**
>
> If you encrypt your files and lose the `.key` file, **it is mathematically impossible to recover your data**. Always keep a backup of your key in a safe location.

-----

## License

This project is open-source. For more details, please read the **[LICENSE](LICENSE)** file.

