# AIRange-CTF-Scripts
I recently had the opportunity to create some CTF Challenges for the [AIRange](https://airange.online/). It was a training platform set by the [Air University Cyber Security Society](http://www.aucss.live) for the students. I developed challenges in the `Ohsint`, `Forensics`, `Cryptography`, `Steganography`, and `Reversing` categories. Here are all the scripts that I used in the development of these challenges.

# Challenge Descriptions

## 4n 0ld Fri3nd
**Catagory:** `Crypto`

In this challange there were three attachments. A `flag-genrator.sh`, `data` file, and `hint.txt`. In the `data` file there are 50 files containing randomly generated strings encrypted with `AES-256-CBC` encryption algorithm. Each file name consists of the prefix `encrypted_data_` followed by a unique identifier generated using the current timestamp hashed with `SHA-256` and then `Base64` encoded. The content of each file is a randomly generated string of length between `8` and `12` characters, encrypted using `AES-256-CBC` algorithm with a key `AUCSS` and saved as a text file. These file were created by the `data-genrator.sh` scripts. Now in the `hint.txt` file there is a story that tells the player about a `SHA-256` hash. So in order to find the correct file contaning the flag you have to calculate `SHA-256` hash of all the files in the `data` folder and then find the one that matches the `SHA-256` hash given in the `hint.txt`. Now inorder to decode the flag you have to reverse the `flag-genrator.sh` script.

## Bing Chilling
**Catagory:** `Forensics`

In this challange there were was image by the name `flag.jpg` was given. I created a python script that takes a `JPG` image file as input, applies a left circular 
shift to the binary data of the image, and then saves the modified image as `flag.jpg`. The 
left circular shift operation involves shifting each byte of the image data from one 
position to the left, with the last byte wrapping around to the beginning. Now in order to fix the image you write a script that would fix the image.
