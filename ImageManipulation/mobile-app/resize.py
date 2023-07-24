from PIL import Image

# Open the original image
for i in range(10):
    print(i)    
    with Image.open('1.png') as img:
        # Resize the image to 1200px by 148px using the ANTIALIAS filter
        resized_img = img.resize((1000, 2200), resample=Image.LANCZOS)    
        # Save the resized image
        resized_img.save(f'resized_{i}.png')

print("Code completed!")