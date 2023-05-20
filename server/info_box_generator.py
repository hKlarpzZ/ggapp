from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageChops

def get_size(height, width):
    if height % 8 == 0:
        new_height = height
    else:
        new_height = height - (height % 8) + 8
    if width % 8 == 0:
        new_width = width
    else:
        new_width = width - (width % 8) + 8
    return new_height, new_width


def create_border(width, height):
    im = Image.new('RGBA', (height + 16, width + 16))
    b = Image.open("./assets/info_box/b.png")
    empty = Image.open("./assets/info_box/empty.png")
    l = Image.open("./assets/info_box/l.png")
    lb = Image.open("./assets/info_box/lb.png")
    lt = Image.open("./assets/info_box/lt.png")
    r = Image.open("./assets/info_box/r.png")
    rb = Image.open("./assets/info_box/rb.png")
    rt = Image.open("./assets/info_box/rt.png")
    t = Image.open("./assets/info_box/t.png")

    height_counter = 0
    while height_counter <= height + 8:
        width_counter = 0
        while width_counter <= width + 8:
            if (height_counter == 0) and (width_counter == 0):
                im.paste(lt, (height_counter, width_counter))
                width_counter += 8
                continue
            if (height_counter == height + 8) and (width_counter == width + 8):
                im.paste(rb, (height_counter, width_counter))
                width_counter += 8
                continue
            if (height_counter == 0) and (width_counter == width + 8):
                im.paste(lb, (height_counter, width_counter))
                width_counter += 8
                continue
            if (height_counter == height + 8) and (width_counter == 0):
                im.paste(rt, (height_counter, width_counter))
                width_counter += 8
                continue
            if height_counter == 0:
                im.paste(l, (height_counter, width_counter))
                width_counter += 8
                continue
            if height_counter == height + 8:
                im.paste(r, (height_counter, width_counter))
                width_counter += 8
                continue
            if width_counter == 0:
                im.paste(t, (height_counter, width_counter))
                width_counter += 8
                continue
            if width_counter == width + 8:
                im.paste(b, (height_counter, width_counter))
                width_counter += 8
                continue
            im.paste(empty, (height_counter, width_counter))
            width_counter += 8
        height_counter += 8
    return im


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


def get_text_size(txt):
    main_font = ImageFont.truetype('./assets/minecraft.ttf', 16)

    img = Image.new('RGBA', size=(1920, 1080))
    I1 = ImageDraw.Draw(img)
    I1.text((0, 1), font=main_font, text=txt)
    new_img = trim(img)
    width = new_img.width
    height = new_img.height

    return height, width, new_img

def get_width(path):
    img = Image.open(path)
    return img.width

def get_height(path):
    img = Image.open(path)
    return img.height


def generate_tab(txt):
    # print("tried to generate tab")
    main_font = ImageFont.truetype('./assets/minecraft.ttf', 16)

    height, width, txt_img = get_text_size(txt)
    height, width = get_size(height + 8, width + 7)
    bg_img = create_border(height, width)
    I1 = ImageDraw.Draw(bg_img)
    I1.text((12, 12), font=main_font, text=txt)

    return bg_img

# print(generate_tab("Упс...\nДанная карточка ещё \nне загрузилась..."))
