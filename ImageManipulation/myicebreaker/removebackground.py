from rembg import remove
from PIL import Image

images = ['sticker01.png', 'sticker02.png', 'sticker03.png', 'sticker04.png', 'sticker05.png', 'sticker06.png', 'sticker07.png', 'sticker08.png', 'sticker09.png', 'sticker10.png', 
          'sticker11.png', 'sticker12.png', 'sticker13.png'] #, 'sticker14.png', 'sticker15.png', 'sticker16.png', 'sticker17.png', 'sticker18.png', 'sticker19.png']
input_path = 'sticker01.png'
outputpath = 'sticker01_output.png'

input = Image.open(input_path)
output = remove(input)
output.save(outputpath)