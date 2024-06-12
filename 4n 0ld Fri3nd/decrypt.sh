#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_name>"
    exit 1
fi

file_name="$1"

if [ ! -f "$file_name" ]; then
    echo "Error: File '$file_name' not found."
    exit 1
fi

# Read the encrypted data from the file
encrypted_string=$(cat "$file_name")

# Decryption flag variable
decryption_key="TRUSTLINE"

# Decrypt the data using OpenSSL
decrypted_string=$(echo "$encrypted_string" | openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -a -k "$decryption_key")

echo "Decrypted flag: $decrypted_string"
