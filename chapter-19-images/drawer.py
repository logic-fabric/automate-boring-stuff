import os

from PIL import Image, ImageDraw, ImageFont


CENTERED_TEXT = "Hello Drawer!"
IMG_SIZE = 400
FONT_FOLDER = '/System/Library/Fonts'
FONT_FILENAME = 'Helvetica.ttc'
LINE_COLOR_1 = 'Violet'
LINE_COLOR_2 = 'CadetBlue'
TEXT_COLOR = 'DarkBlue'
STEP = 24


if __name__ == '__main__':
    img = Image.new('RGBA', (IMG_SIZE, IMG_SIZE), 'white')
    drawer = ImageDraw.Draw(img)

    for step in range(0, IMG_SIZE - 1, STEP):
        if (step // STEP) % 2:
            line_color = LINE_COLOR_1
        else:
            line_color = LINE_COLOR_2
        
        drawer.line(
            [
                (step, 0), 
                (0, IMG_SIZE - 1 - step)
            ],
            fill=line_color,
        )
        drawer.line(
            [
                (IMG_SIZE - 1 - step, 0), 
                (IMG_SIZE - 1, IMG_SIZE - 1 - step)
            ],
            fill=line_color,
        )
        drawer.line(
            [
                (step, IMG_SIZE - 1), 
                (0, step)
            ],
            fill=line_color,
        )
        drawer.line(
            [
                (step, IMG_SIZE - 1), 
                (IMG_SIZE - 1, IMG_SIZE - 1 - step)
            ],
            fill=line_color,
        )

    font = ImageFont.truetype(os.path.join(FONT_FOLDER, FONT_FILENAME), 32)
    text_width, text_height = drawer.textsize(CENTERED_TEXT, font=font)
    pos_x = (IMG_SIZE - text_width) // 2
    pos_y = (IMG_SIZE - text_height) // 2
    drawer.text((pos_x, pos_y), CENTERED_TEXT, fill=TEXT_COLOR, font=font)

    img.save('drawing.png')
