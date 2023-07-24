from PIL import Image

def add_watermark(input_image_path, output_image_path, watermark_image_path, transparency=100):
    try:
        # Open the input image and the watermark image
        input_image = Image.open(input_image_path)
        watermark = Image.open(watermark_image_path)
        watermark = watermark.resize((50, 50), resample=Image.LANCZOS) 

        # If the input image has an alpha channel, convert the watermark image to RGBA
        if input_image.mode in ('RGBA', 'LA'):
            watermark = watermark.convert("RGBA")

        # Adjust watermark transparency
        if 0 <= transparency <= 100:
            alpha = watermark.split()[3]
            alpha = alpha.point(lambda p: p * transparency / 100)
            watermark.putalpha(alpha)

        # Calculate the position for the bottom right corner
        position = (input_image.width - watermark.width*2, input_image.height - watermark.height*2)

        # Paste the watermark on the input image
        input_image.paste(watermark, position, watermark)

        # Save the result as the output image
        input_image.save(output_image_path)
        print("Watermark added successfully.")
    except Exception as e:
        print("Error:", e)

# Example usage:
# Example usage:
input_image_path = "1.png"
output_image_path = "watermark.png"
watermark_image_path = "3.png"
# position = (50, 50)  # Position of the watermark on the input image (top-left corner)
transparency = 50    # Set the transparency level (0 to 100)

add_watermark(input_image_path, output_image_path, watermark_image_path, transparency)

