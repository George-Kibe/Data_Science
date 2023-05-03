from PIL import Image

# Open the original image
with Image.open('wallpaper1.jpg') as img:
    # Set the region to crop
    left = 0
    top = 100
    right = 800
    bottom = 400
    
    # Crop the image
    cropped_img = img.crop((left, top, right, bottom))
    
    # Save the cropped image
    cropped_img.save('cropped_image.jpg')