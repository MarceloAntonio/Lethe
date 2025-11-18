FROM python:latest

COPY . /EncryptAndDecryptFolders 

WORKDIR /EncryptAndDecryptFolders 

RUN pip install --no-cache-dir -r requirements.txt

