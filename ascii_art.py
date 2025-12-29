from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, max_width=60, max_height=40):
    w, h = image.size
    
    # Calculate aspect ratio
    aspect_ratio = h / w
    width_based_height = int(max_width * aspect_ratio * 0.45)
    height_based_width = int(max_height / (aspect_ratio * 0.45))
    if width_based_height <= max_height:
        # Width is the limiting factor
        final_width = max_width
        final_height = width_based_height
    else:
        final_width = height_based_width
        final_height = max_height
    
    return image.resize((final_width, final_height))

def to_grayscale(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels)
    return ascii_str

def image_to_ascii(path, max_width=60, max_height=40):
    image = Image.open(path)
    image = resize_image(image, max_width, max_height)
    image = to_grayscale(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width

    ascii_img = "\n".join(
        ascii_str[i:i + img_width]
        for i in range(0, len(ascii_str), img_width)
    )
    return ascii_img

print(image_to_ascii("Face.png", max_width=35, max_height=20))