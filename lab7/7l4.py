def add_watermark(input_image_path, output_folder, watermark_text, position=(10, 10), font_size=36, font_color=(255, 255, 255, 128)):
    img = Image.open(input_image_path)
    width, height = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    text_width, text_height = draw.textsize(watermark_text, font=font)
    text_position = (width - text_width - position[0], height - text_height - position[1])

    draw.text(text_position, watermark_text, font=font, fill=font_color)

    filename = os.path.basename(input_image_path)
    output_path = os.path.join(output_folder, f"watermarked_{filename}")
    img.save(output_path)
    print(f"Водяной знак добавлен к изображению и сохранен как {output_path}")

def main():

    input_folder = "input_images"
    output_folder = "output_images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    watermark_text = "Your Watermark"

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            add_watermark(image_path, output_folder, watermark_text)

if __name__ == "__main__":
    main()