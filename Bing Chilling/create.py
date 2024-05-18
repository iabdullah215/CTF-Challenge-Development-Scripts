#!/usr/bin/env python3

import sys

def apply_right_circular_shift(data):
    shifted_data = bytearray()
    for i in range(len(data)):
        shifted_data.append(data[(i - 1) % len(data)])
    return shifted_data

def save_modified_image(image, modified_data):
    try:
        with open('flag_inverse.jpg', 'wb') as output_file:
            output_file.write(modified_data)
        print("\nModified image saved as flag_inverse.jpg")
    except FileNotFoundError:
        print(f"Error: File '{image}' not found!")

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <image.jpg>".format(sys.argv[0]))
        sys.exit(1)
    
    image = sys.argv[1]

    try:
        with open(image, 'rb') as f:
            image_data = f.read()

        # Apply right circular shift (inverse operation)
        modified_data = apply_right_circular_shift(image_data)
        
        # Save modified image
        save_modified_image(image, modified_data)

    except FileNotFoundError:
        print(f"Error: File '{image}' not found!")

if __name__ == "__main__":
    main()
