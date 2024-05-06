

holiday_cards = {
    "День рождения": "birthday_card.jpg",
    "Новый год": "new_year_card.jpg",
    "День Святого Валентина": "valentines_day_card.jpg",
    "Международный женский день": "womens_day_card.jpg",
}

def add_text_to_card(image_path, name, output_folder):

    img = Image.open(image_path)
    width, height = img.size

    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default()

    text = f"{name}, поздравляю!"

    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((width - text_width) // 2, height - text_height - 20)

    draw.text(text_position, text, font=font, fill="white")

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, f"modified_{filename[:-4]}.png")
    img.save(output_path)
    print(f"Открытка с текстом сохранена как {output_path}")

def main():
    holiday = input("Введите название праздника, для которого вам нужна открытка: ")

    name = input("Введите имя того, кого вы хотите поздравить: ")

    if holiday in holiday_cards:
        card_filename = holiday_cards[holiday]
        image_path = card_filename
        add_text_to_card(image_path, name, ".")
    else:
        print("Извините, у нас нет открытки для этого праздника.")

if __name__ == "__main__":
    main()