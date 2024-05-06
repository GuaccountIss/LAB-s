def resize_image(image_path, output_folder, scale_factor):

    img = Image.open(image_path)

    new_width = img.width // scale_factor
    new_height = img.height // scale_factor

    resized_img = img.resize((new_width, new_height))

    filename = os.path.basename(image_path)
    resized_img_path = os.path.join(output_folder, f"resized_{filename}")
    resized_img.save(resized_img_path)
    print(f"Уменьшенная копия сохранена как {resized_img_path}")

def mirror_image(image_path, output_folder):
    img = Image.open(image_path)

    mirrored_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
    mirrored_horizontal_path = os.path.join(output_folder, f"mirrored_horizontal_{os.path.basename(image_path)}")
    mirrored_horizontal.save(mirrored_horizontal_path)
    print(f"Горизонтальный зеркальный образ сохранен как {mirrored_horizontal_path}")

    mirrored_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
    mirrored_vertical_path = os.path.join(output_folder, f"mirrored_vertical_{os.path.basename(image_path)}")
    mirrored_vertical.save(mirrored_vertical_path)
    print(f"Вертикальный зеркальный образ сохранен как {mirrored_vertical_path}")

def main():

    input_folder = "input_images"

    output_folder = "output_images"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            # Создаем уменьшенную копию изображения
            resize_image(image_path, output_folder, 3)
            # Получаем зеркальные образы изображения
            mirror_image(image_path, output_folder)

if __name__ == "__main__":
    main()