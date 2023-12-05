
# import sys
# from PIL import Image

# images = []

# for arg in sys.argv[1:]:
#     image = Image.open(arg)
#     images.append(image)

# images[0].save(
#     "costumes.gif", save_all=True, append_images=images[1:], duration=400, loop=0
# )




import sys
from PIL import Image

images = []

# Check if there are command-line arguments
if len(sys.argv) < 2:
    print("Usage: python test1.py image1_path image2_path ...")
    sys.exit(1)

# Load images from command-line arguments
for arg in sys.argv[1:]:
    try:
        image = Image.open(arg)
        images.append(image)
    except Exception as e:
        print(f"Error loading image from {arg}: {e}")

# Check if there are at least two images to create a GIF
if len(images) < 2:
    print("Please provide at least two valid images to create a GIF.")
    sys.exit(1)

# Resize images to a specific width and height (e.g., 800x600)
width, height = 800, 600
resized_images = [img.resize((width, height)) for img in images]

# Save the GIF with custom filenames
output_filename = "costumes.gif"
resized_images[0].save(
    output_filename,
    save_all=True,
    append_images=resized_images[1:],
    duration=400,
    loop=0
)

print(f"GIF saved as {output_filename}")
