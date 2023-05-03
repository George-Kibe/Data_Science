from PIL import Image, ImageEnhance

# Open the original image
with Image.open('resized_wallpaper.png') as img:
    # Create a brightness enhancer object
    enhancer = ImageEnhance.Brightness(img)
    
    # Increase the brightness by a factor of 1.5
    brighter_img = enhancer.enhance(2.5)
    
    # Save the brighter image
    brighter_img.save('brighter_wallpaper.png')
