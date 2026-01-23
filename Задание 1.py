#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def add_products():
    """
    Добавить новый товар в список
    """
    product = input("Введите название товара: ")
    shop = input("Введите название магазина: ")
    price = float(input("Введите стоимость: "))

    return{
        'товар': product,
        'магазин': shop,
        'цена': price
    }


def list_products(products):
    """
    Отобразить список товаров
    """
    if products:
        print("Все товары:")
        for p in products:
            print(f"{p['магазин']} - {p['товар']} - {p['цена']} руб.")


def search_products(products):
    """
    Найти товары по названию магазина
    """
    search = input("Введите магазин для поиска: ")
    found = [p for p in products if p['магазин'].lower() == search.lower()]

    if found:
        print(f"Товары в магазине '{search}':")
        for p in found:
            print(f"{p['товар']} - {p['цена']} руб.")
    else:
        print(f"Магазин '{search}' не найден.")


def main():
    """
    Главная функция программы
    """
    products = []

    while True:
        command = input(">>> ").lower()

        match command:
            case 'exit':
                break

            case 'add':
                goods = add_products()
                products.append(goods)
                if len(products) > 1:
                    products.sort(key=lambda item: item.get('магазин', ''))

            case 'list':
                list_products(products)

            case 'search':
                search_products(products)

            case 'help':
                print("Список команд:\n")
                print("add - добавить товар;")
                print("list - вывести список товаров;")
                print("search - вывести информацию о товарах, продающихся в данном магазине;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")

            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)
                return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
