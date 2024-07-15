from PIL import Image
import sys

def image_to_rawdata(input_image_path, output_data_path, width=220, height=220):
    img = Image.open(input_image_path).convert("L") 

    # Resize the image
    img = img.resize((width, height))

    threshold = 128

    # Prepare the data
    image_data = []
    for i in range(height):
        row = []
        for j in range(width):
            pixel_value = img.getpixel((j, i))
            if pixel_value > threshold:
                row.append("74")
            else:
                row.append("0")
        image_data.append(row)

    with open(output_data_path, "w") as f:
        for row in image_data:
            f.write(" ".join(row) + "\n")

    print(f"Data has been written to {output_data_path}")

if len(sys.argv) != 3:
    print("Usage: python script.py <input_image_path> <output_data_path>")
else:
    input_image_path = sys.argv[1]
    output_data_path = sys.argv[2]
    image_to_rawdata(input_image_path, output_data_path)
