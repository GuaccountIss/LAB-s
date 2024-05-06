def main():

    image_path = "your_image.jpg"

    img = Image.open(image_path)

    print("Размер изображения:", img.size)

    print("Формат изображения:", img.format)

    print("Цветовая модель:", img.mode)

    img.show()

if __name__ == "__main__":
    main()