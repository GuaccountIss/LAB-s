def apply_filter_to_images(input_folder, output_folder, filter_type):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            img = Image.open(os.path.join(input_folder, filename))

            filtered_img = img.filter(filter_type)

            output_path = os.path.join(output_folder, filename)
            filtered_img.save(output_path)

            print(f"Фильтр успешно применен к файлу {filename} и сохранен как {output_path}")


def main():
    input_folder = "input_images"
    output_folder = "output_images"
    filter_type = ImageFilter.SHARPEN
    apply_filter_to_images(input_folder, output_folder, filter_type)


if __name__ == "__main__":
    main()