# CTF Challenge Development Scripts
I recently have been developing CTF Challenges for many platforms. I developed challenges in the `Ohsint`, `Forensics`, `Cryptography`, `Steganography`, and `Reversing` categories. Here are some of the scripts that I used in the development of those challenges.

# Challenge Descriptions

## 4n 0ld Fri3nd
**Catagory:** `Crypto`

**Patforms:** TRUSTLINE

In this challenge there were five attachments. A `phesudocode.txt`, `file` directory, `plane ticket.png`, `medical slip.png`, `crypto wallet.png` and `hint.txt`. In the `file` directory there are 100 files containing randomly generated strings encrypted with `AES-256-CBC` encryption algorithm. Each file name consists of the prefix `encrypted_data_` followed by a unique identifier generated using the current timestamp hashed with `SHA-256` and then `Base64` encoded. The content of each file is a randomly generated string of length between `8` and `12` characters, encrypted using `AES-256-CBC` algorithm with a key `TRUSTLINE` and saved as a text file. These file were created by the `file-genrator.sh` scripts. Now in the `hint.txt` file and the images point towards a story that tells the player about a `SHA-256` hash. So in order to find the correct file contaning the flag you have to calculate `SHA-256` hash of all the files in the `file` folder and then find the one that matches the `SHA-256` hash given in the `crypto wallet.png`. Now inorder to decode the flag you have to reverse the `flag-genrator.sh` phesudocode given in the `phesudocode.txt`.

**Flag**

```console
┌──(MnM@kali)-[~/Desktop/CTFs/TRUSTLINE/Crypto]
└─$ ./decrypt.sh files/encrypted_data_ZThlM2Qw.txt     
Decrypted flag: TRUSTLINE{Working_hard_is_the_key_to_success_my_fr1end}
```

## Bing Chilling
**Catagory:** `Forensics`

**Patforms:** AIRange

In this challenge there was an image by the name `flag.jpg` given. I created a python script that takes a `JPG` image file as input, applies a left circular shift to the binary data of the image, and then saves the modified image as `flag.jpg`. The left circular shift operation involves shifting each byte of the image data from one position to the left, with the last byte wrapping around to the beginning. Now in order to fix the image you write a script that would fix the image.

## T3r1pl3 Thr34t
**Catagory:** `Crypto`

**Patforms:** TRUSTLINE

In this challenge a script is given that you have reverse inorder to get the flag. The script begins by reading the contents of a file named `flag.txt`, which contains the `flag`. Then, it generates three large prime numbers (`p`, `q`, and `r`) with `1024 bits` each using the `getPrime` function from the `Crypto.Util.number` library. These prime numbers are then used to calculate three RSA modulo (`n1`, `n2`, and `n3`) by multiplying pairs of these prime numbers together. After generating the modulo, it sets `e` to `65537` which is a commonly used value in RSA encryption. Then, it converts the `flag` into a long integer using the `bytes_to_long` function. Next, the script iterates over each modulus and encrypts the `flag` using RSA encryption. Each modulus `n` raises the plaintext to the power of `e` modulo `n`. This operation is repeated for each modulus, resulting in multiple Cipher Texts. Finally, the script prints the encrypted message to the terminal and writes the generated public keys (`n1`, `n2`, and `n3`), the public exponent `e`, and the cipher text `c` to a file named `public-key.txt`.

**Flag**

```console
┌──(MnM@kali)-[~/Desktop/CTFs/TRUSTLINE/Crypto]
└─$ python3 decrypt.py
TRUSTLINE{1_gu3ss_tr1pl3_rs4_1snt_tr1pl3_s3cur3}
```

## Tweak
**Catagory:** `Reversing`

**Patforms:** AIRange

In this challenge a C++ script was given which employs a Caesar cipher encryption technique. It defines a function `Flag` to encrypt a given string using a provided key. The main function initializes a `key` array with zeros and encrypts the string using this `key`, resulting in no encryption due to the key being all zeros. Therefore, the output remains the same as the input string. The player has to change the key in a way that it would change the string into a flag. The accurate key is provided blow.

```C++
const int key[] = {0, 4, 0, -9, 0, 0, 8, 0, -14, 0, 21, 0, -9, 0, -6, 0, -2, 0, 4, 0}
```

**Flag**

```console
┌──(MnM@kali)-[~/Desktop/CTFs/AIRange/Reverse]
└─$ ./script.cpp
Your Flag Is: flagfumbledtilldeath
```

## Os and 1s
**Catagory:** `BarCode`

**Patforms:** Hackathon Training Workshop 2024

In this challenge a `rawdata.txt` file has been given as a lead. In this file there is RGB value of an image. This file was created by using the `break.py` script. In order to convert the RGB values into image you have to write a script like `create.py`. Upon running the file you'll have an image of a BarCode and after scanning this BarCode you'll have the flag.

## Double Trouble
**Catagory:** `Crypto`

**Patforms:** Hackathon Training Workshop 2024

In this challenge a script is given that you have reverse inorder to get the flag. The script begins by reading the contents of a file named `flag.txt`, which contains the `flag`. Then, it generates two large prime numbers (`p` and `q`) with `1024 bits` each using the `getPrime` function from the `Crypto.Util.number` library. These prime numbers are then used to calculate two RSA modulo (`n1` and `n2`) by multiplying pairs of these prime numbers together. After generating the modulo, it sets `e` to `65537` which is a commonly used value in RSA encryption. Then, it converts the `flag` into a long integer using the `bytes_to_long` function. Next, the script iterates over each modulus and encrypts the `flag` using RSA encryption. Each modulus `n` raises the plaintext to the power of `e` modulo `n`. This operation is repeated for each modulus, resulting in multiple Cipher Texts. Finally, the script prints the encrypted message to the terminal and writes the generated public keys (`n1` and `n2`), the public exponent `e`, and the cipher text `c` to a file named `public-key.txt`.

**Flag:**

```console
┌──(MnM@kali)-[~/Desktop/CTFs/Hackathon/Crypto]
└─$ python3 decrypt.py
flag{double_R54_i5_double_h4rd}
```

## Baby-step Giant-step
**Catagory:** `Crypto`

**Patforms:** Hackathon Training Workshop 2024

In this challenge the player has to perfom meet-in-the-middle attack in order to get the flag (value of `X`). Upon running the `flager.py` script player would get the flag as follow.

```console
┌──(MnM@kali)-[~/Desktop/CTFs/Hackathon/Crypto]
└─$ python3 flager.py
finding x...
Flag =  375374217830
```
