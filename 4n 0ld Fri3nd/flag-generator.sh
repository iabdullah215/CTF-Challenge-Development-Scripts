#!/bin/bash

generate_random_string() {
    characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    length=$(( RANDOM % 5 + 8 ))

    string=''
    for (( i=0; i<$length; i++ )); do
        string+=${characters:RANDOM%${#characters}:1}
    done

    echo "$string"
}

# Loop only once
for (( i=1; i<=1; i++ )); do
    file_name="encrypted_data_$(date +%s%N | sha256sum | base64 | head -c 8).txt"

    random_string=$(generate_random_string)

    encrypted_string=$(echo "$random_string" | openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -salt -a -k AUCSS)

    echo "$encrypted_string" > "$file_name"

    echo "File '$file_name' created with encrypted data."
done
