from PIL import Image
import sys

def rawdata_to_image(input_data_path, output_image_path):

    image_text = []

    with open(input_data_path, "r") as f:
        for line in f.readlines():
            line = line.rstrip()
            image_text.append(line.split(" "))

    height = len(image_text)
    width = len(image_text[0])

    img = Image.new(mode="RGB", size=(width, height))

    white = (255, 255, 255)
    black = (0, 0, 0)

    for i in range(height):
        for k in range(width):
            if image_text[i][k] == "74":
                img.putpixel((k, i), white)
            else:
                img.putpixel((k, i), black)

    img.save(output_image_path)
    print(f"Image has been saved to {output_image_path}")

if len(sys.argv) != 3:
    print("Usage: python script.py <input_data_path> <output_image_path>")
else:
    input_data_path = sys.argv[1]
    output_image_path = sys.argv[2]
    rawdata_to_image(input_data_path, output_image_path)
