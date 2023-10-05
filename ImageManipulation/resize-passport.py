from PIL import Image

# Open the original image
with Image.open('George-image.jpeg') as img:
    # Resize the image to 1200px by 148px using the ANTIALIAS filter
    resized_img = img.resize((600, 600), resample=Image.LANCZOS)    
    # Save the resized image
    resized_img.save('resized-passport.jpeg')