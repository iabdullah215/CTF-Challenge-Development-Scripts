#!/bin/bash

# Function to generate a random string (no longer used)
generate_random_string() {
    characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    length=$(( RANDOM % 5 + 8 ))

    string=''
    for (( i=0; i<$length; i++ )); do
        string+=${characters:RANDOM%${#characters}:1}
    done

    echo "$string"
}

# Encryption flag variable
flag="flag{3456jhbr5ijigr657yuhjbhfgtr57689uiojbhgcy6}"

# Loop only once
for (( i=1; i<=1; i++ )); do
    file_name="encrypted_data_$(date +%s%N | sha256sum | base64 | head -c 8).txt"

    # Encrypt the flag variable
    encrypted_string=$(echo "$flag" | openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -salt -a -k TRUSTLINE)

    echo "$encrypted_string" > "$file_name"

    echo "File '$file_name' created with encrypted data."
done
