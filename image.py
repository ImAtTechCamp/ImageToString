from PIL import Image

# Load and convert image to grayscale
input_image_path = "input_image.png"
output_text_path = "output_brightness.txt"

# Open the image and convert it to grayscale
image = Image.open(input_image_path).convert("L")

# Resize the image if needed to fit within desired dimensions (optional)
# image = image.resize((width, height))

# Scale each pixel's brightness to a value between 0 and 100
pixels = [(pixel * 100) // 255 for pixel in image.getdata()]

# Write the result to a text file with comma-separated values and no line breaks
with open(output_text_path, "w") as file:
    file.write(",".join(map(str, pixels)))
print("Done")
