from PIL import Image, ImageDraw, ImageFont, ImageColor
import logging

# 设置日志配置
logging.basicConfig(level=logging.DEBUG)


def create_cover(size, bg_options, bg_color, text, text_color, font_choice, font_size, angle, stroke_width,
                 stroke_color, gradient=None, bg_image=None):
    logging.info("Starting cover creation process...")
    font_paths = {
        "站酷快乐体": "fonts/站酷快乐体.ttf",
        "站酷庆科黄油体": "fonts/站酷庆科黄油体.ttf",
        "站酷文艺体": "fonts/站酷文艺体.ttf",
    }
    font = ImageFont.truetype(font_paths[font_choice], font_size)

    if bg_options == "上传图片" and bg_image is not None:
        image = Image.open(bg_image)
        image = image.resize(size)
        logging.info("Background image uploaded and resized.")
    else:
        image = Image.new('RGB', size, bg_color if bg_options == "纯色" else (255, 255, 255))
        logging.info("Background set to solid color or default white.")
        if bg_options == "渐变色" and gradient:
            draw = ImageDraw.Draw(image)
            draw_gradient(draw, size, gradient)
            logging.info("Gradient background applied.")

    # Prepare text layer for rotation
    text_image = Image.new('RGBA', size, (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_image)

    text_bbox = text_draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = ((size[0] - text_width) / 2, (size[1] - text_height) / 2)

    # Draw stroke
    if stroke_width > 0:
        logging.info("Applying text stroke.")
        for dx in range(-stroke_width, stroke_width + 1):
            for dy in range(-stroke_width, stroke_width + 1):
                text_draw.text((text_position[0] + dx, text_position[1] + dy), text, font=font, fill=stroke_color)

    # Draw text
    text_draw.text(text_position, text, font=font, fill=text_color)

    # Rotate text image around its center
    if angle != 0:
        text_image = text_image.rotate(angle, expand=1, center=text_position, resample=Image.BICUBIC)
        logging.info("Text rotated around its center.")

    # Merge text image with background
    image.paste(text_image, (0, 0), text_image)

    logging.info("Cover creation process completed.")
    return image


def draw_gradient(draw, size, gradient):
    start_color, end_color = gradient[1], gradient[2]
    for i in range(size[1]):
        inter_color = interpolate(start_color, end_color, size[1], i)
        draw.line([(0, i), (size[0], i)], fill=inter_color)
    logging.info("Gradient drawn on image.")


def interpolate(start_color, end_color, steps, step):
    start_rgb = ImageColor.getrgb(start_color)
    end_rgb = ImageColor.getrgb(end_color)
    r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * step / steps)
    g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * step / steps)
    b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * step / steps)
    return (r, g, b)

def load_gradient():
    return [
        ("Antarctica", "#D8B5FF", "#1EAE98"),
        ("Bloody Mary", "#FF512F", "#DD2476"),
        ("Cactus", "#C6EA8D", "#FE90AF"),
        ("Celestial", "#C33764", "#1D2671"),
        ("Clean Mirror", "#93A5CF", "#E4EfE9"),
        ("Eternal Constance", "#09203F", "#537895"),
        ("Green Beach", "#02AABD", "#00CDAC"),
        ("Juicy Peach", "#FFECD2", "#FCB69F"),
        ("Kashmir", "#614385", "#516395"),
        ("Luscious Lime", "#009245", "#FCEE21")
        # Add more gradients here
    ]