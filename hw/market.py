from datetime import datetime
from logger import logger_decorator

class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.drink_titles = set(drink.title for drink in wines + beers if drink.title is not None)
        self.drinks = [drink for drink in wines + beers if drink.title is not None]

    @logger_decorator
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.drink_titles

    @logger_decorator
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return sorted(self.drink_titles)

    @logger_decorator
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        drinks_by_date = []
        for drink in self.drinks:
            if None not in (drink.production_date, from_date, to_date):
                if datetime.strptime(to_date, "%d.%m.%Y") >= drink.production_date >= datetime.strptime(from_date, "%d.%m.%Y"):
                    drinks_by_date.append(drink)
        
        return drinks_by_date
