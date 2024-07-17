#!/bin/bash

Flag() {
    local odd="$1"
    local key=("${@:2}")
    local length=${#key[@]}
    local flag=""
    
    for (( i=0; i<length; i++ )); do
        local char="${odd:$i:1}"
        local ascii=$(printf "%d" "'$char")
        local new_char=$(( (ascii - 97 + key[i] + 26) % 26 + 97 ))
        flag+=$(printf "\x$(printf %x $new_char)")
    done
    
    echo "$flag"
}

# Define the key array
key=(0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0)

# Call the Flag function
flag=$(Flag "fhapfuebzeitrlrdgaph" "${key[@]}")

echo "Your Flag Is: $flag"
