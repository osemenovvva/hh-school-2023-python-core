from wine import Wine
from beer import Beer
from market import Market


if __name__ == '__main__':

    wines = [
            Wine('Белое', '11.12.2023'),
            Wine('Красное', '11.10.2023'),
            Wine('Розовое', '11.05.2023'),
            Wine('Игристое', '11.02.2023'),
            Wine(),
            Wine(title = 'Брют'),
            Wine(production_date = '11.06.2023')
    ]

    beers = [
            Beer('Жигулевское', '20.01.2023'),
            Beer('Балтика', '20.07.2023'),
            Beer('Heiniken', '20.11.2023'),
            Beer('Bud', '20.12.2023')
    ]

    market = Market(wines, beers)

    # Проверка наличия названия в списке напитков
    assert(market.has_drink_with_title('Игристое'))
    assert(not market.has_drink_with_title('Оболонь'))
    assert(not market.has_drink_with_title())

    # Вывод списка напитков
    drinks_sorted_by_title = market.get_drinks_sorted_by_title()
    for drink in drinks_sorted_by_title:
        print(drink)
    
    # Вывод напитков по дате
    drinks_by_date_test1 = market.get_drinks_by_production_date('01.05.2023', '20.10.2023')
    for test1 in drinks_by_date_test1:
        print(test1.title)
    
    drinks_by_date_test2 = market.get_drinks_by_production_date()
    for test2 in drinks_by_date_test2:
        print(test2.title)

