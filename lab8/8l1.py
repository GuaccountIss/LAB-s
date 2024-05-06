def crop_image(input_image_path, output_image_path, crop_area):
    img = Image.open(input_image_path)

    cropped_img = img.crop(crop_area)
    cropped_img.save(output_image_path)
    print(f"Область изображения успешно вырезана и сохранена как {output_image_path}")

def main():
    input_image_path = "input_image.jpg"


    output_image_path = "cropped_image.jpg"

    )
    crop_area = (100, 100, 400, 400)

    crop_image(input_image_path, output_image_path, crop_area)

if __name__ == "__main__":
    main()