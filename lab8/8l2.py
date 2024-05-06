
holiday_cards = {
    "День рождения": "birthday_card.jpg",
    "Новый год": "new_year_card.jpg",
    "День Святого Валентина": "valentines_day_card.jpg",
    "Международный женский день": "womens_day_card.jpg",

}

def display_card(holiday):

    if holiday in holiday_cards:

        card_filename = holiday_cards[holiday]
        with open(card_filename, "rb") as f:
            display(Image.open(f))
    else:
        print("Извините, у нас нет открытки для этого праздника.")

def main():
    holiday = input("Введите название праздника, для которого вам нужна открытка: ")

    display_card(holiday)

if __name__ == "__main__":
    main()