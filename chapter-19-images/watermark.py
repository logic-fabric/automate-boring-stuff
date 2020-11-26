"""Script that:
- create a monochrome watermark from a logo containng transparency
- standardize the sizes of all '*.jpg' and '*.png' images before adding the watermark
- save the resized and watermarked images in a dedicated directory
"""

import os

from PIL import Image, ImageColor


LOGO_FILENAME = 'logo.png'

STANDARD_WIDTH = 400

WATERMARK_COLOR = 'lightblue'
WATERMARK_FILENAME = 'watermark.png'
WATERMARK_WIDTH = STANDARD_WIDTH // 5

WATERMARKED_DIR = 'watermarked'


def get_watermark(logo_file: str) -> Image:
    logo = Image.open(logo_file)
    width, height = logo.size

    watermark = logo.resize(
        (WATERMARK_WIDTH, int(height * (WATERMARK_WIDTH / width)))
    )
    return watermark

def colorize_watermark(watermark: Image, color: str) -> Image:
    width, height = watermark.size

    try:
        for x in range(width):
            for y in range(height):
                if watermark.getpixel((x, y)) != (0, 0, 0, 0):
                    watermark.putpixel(
                        (x, y), 
                        ImageColor.getcolor(color, 'RGBA'),
                    )
    except ValueError:
        print(f"'{color}' is not an existing HTML color.")
    
    return watermark

def standardize_size(img: Image) -> Image:
    width, height = img.size

    resized_img = img.resize(
        (STANDARD_WIDTH, int(height * (STANDARD_WIDTH / width)))
    )
    return resized_img

def watermark_img(img: Image) -> Image:
    watermark = Image.open(WATERMARK_FILENAME)

    img_width, img_height = img.size
    watermark_width, watermark_height = watermark.size

    img.paste(
        watermark,
        (img_width - watermark_width, img_height - watermark_height),
        watermark
    )
    return img
    

if __name__ == '__main__':
    watermark = get_watermark(LOGO_FILENAME)
    watermark = colorize_watermark(watermark, WATERMARK_COLOR)
    watermark.save(WATERMARK_FILENAME)

    os.mkdir(WATERMARKED_DIR)

    for filename in os.listdir('.'):
        if (
            filename.endswith('.jpg') 
            or filename.endswith('.png') 
            and filename not in {LOGO_FILENAME, WATERMARK_FILENAME}
        ):
            img = Image.open(filename)

            img = standardize_size(img)
            watermarked = watermark_img(img)

            watermarked.save(f'{WATERMARKED_DIR}/{filename}')
