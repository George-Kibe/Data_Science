from PIL import Image

# Open the original image
with Image.open('wallpaper2.png') as img:
    # Resize the image to 1200px by 148px using the ANTIALIAS filter
    resized_img = img.resize((1200, 148), resample=Image.LANCZOS)    
    # Save the resized image
    resized_img.save('resized_wallpaper.png')