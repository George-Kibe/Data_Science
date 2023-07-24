from PIL import Image

def join_images_horizontally(image_paths):
    images = [Image.open(img_path) for img_path in image_paths]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_image = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for image in images:
        new_image.paste(image, (x_offset, 0))
        x_offset += image.width

    return new_image

# Example usage:
portrait_image_paths = ["7.png", "8.png", "9.png", "6.png"]
result_image = join_images_horizontally(portrait_image_paths)
result_image.save("landscape_image1.png")

print("Code completed")