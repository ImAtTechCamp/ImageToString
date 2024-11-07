from PIL import Image

# Specify the dimensions of the original image
width, height = 480, 360  # Replace with the original dimensions
input_text_path = "output_brightness.txt"
output_image_path = "reconstructed_image.png"

# Read the brightness values from the text file
with open(input_text_path, "r") as file:
    brightness_values = list(map(int, file.read().split(',')))

# Scale values back from 0-100 range to 0-255 for grayscale
pixels = [(value * 255) // 100 for value in brightness_values]

# Create a new grayscale image
image = Image.new("L", (width, height))
image.putdata(pixels)

# Save the reconstructed image
image.save(output_image_path)
