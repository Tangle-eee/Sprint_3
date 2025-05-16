import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # 1. Геттеры
    # В чеке печатают названия товаров и их количество. Но атрибуты name_items и number_items — приватные. К ним нельзя обратиться напрямую.
    # Напиши геттеры, которые получают значения name_items и number_items. Используй декоратор @property.
    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    # 2. Добавление товара в чек
    # Напиши метод add_item_to_cheque. Он добавляет товары в чек.
    # В качестве аргумента метод принимает название товара — name.
    # В теле метода напиши условия:
    # - Если в названии товара 0 или больше 40 символов, выводится исключение ValueError. Оно печатает сообщение: 'Нельзя добавить товар, если в его названии нет символов или их больше 40'.
    # - Если названия товара нет в списке item_price, выводится исключение NameError с текстом 'Позиция отсутствует в товарном справочнике'.
    # - В остальных случаях метод добавляет товар в name_items и увеличивает значение number_items на 1.
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

    # 3. Удаление товара из чека
    # Напиши метод delete_item_from_check. Он убирает товары из чека. Метод принимает аргумент name.
    # В теле используй условие:
    # - Если товара нет в списке name_items, выводится исключение NameError с текстом 'Позиция отсутствует в чеке';
    # - В остальных случаях метод удаляет товар из name_items и уменьшает number_items на 1.
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    # 4. Подсчёт суммы с учётом скидки
    # Напиши метод check_amount. Он считает общую сумму покупок.
    # Логика такая: метод содержит пустой список total и добавляет в него цены товаров из списка name_items. Их он берёт из словаря item_price.
    # Ещё в методе есть условие:
    # - Если в чеке больше 10 товаров, сумма чека возвращается со скидкой 10%;
    # - В остальных случаях возвращается полная сумма.
    def check_amount(self):
        total = [self.__item_price[item] for item in self.__name_items]
        total_sum = sum(total)
        if self.__number_items > 10:
            return round(total_sum * 0.9, 2)
        return total_sum

    # 5. НДС со ставкой 20%
    # Напиши метод twenty_percent_tax_calculation. Он рассчитывает НДС товаров, у которых налоговая ставка 20%.
    # В теле метода:
    # - Пустой список twenty_percent_tax. Сюда метод добавляет товары из списка name_items, если в словаре tax_rate у них указана ставка 20%.
    # - Пустой список total. Сюда метод добавляет цены товаров, которые включили в twenty_percent_tax.
    # Метод должен вернуть общую сумму НДС для позиций чека с максимальной ставкой. Отталкивайся от формулы: НДС = стоимость товара * 0,2.
    # При расчете не забудь учесть скидку при количестве товаров больше 10.
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = [item for item in self.__name_items if self.__tax_rate[item] == 20]
        total = [self.__item_price[item] for item in twenty_percent_tax]
        total_sum = sum(total)
        if self.__number_items > 10:
            total_sum *= 0.9
        return round(total_sum * 0.2, 2)

    # 6. НДС со ставкой 10%
    # Напиши метод ten_percent_tax_calculation. Он рассчитывает НДС товаров, у которых ставка 10%.
    # В теле метода:
    # - Пустой список ten_percent_tax. Сюда метод добавляет товары из списка name_items, если в словаре tax_rate у них указана ставка 10%.
    # - Пустой список total. Сюда метод добавляет цены товаров, которые включили в ten_percent_tax.
    # Метод должен вернуть общую сумму НДС для позиций чека со ставкой 10%. Отталкивайся от формулы: НДС = стоимость товара * 0,1.
    # При расчете не забудь учесть скидку при количестве товаров больше 10.
    def ten_percent_tax_calculation(self):
        ten_percent_tax = [item for item in self.__name_items if self.__tax_rate[item] == 10]
        total = [self.__item_price[item] for item in ten_percent_tax]
        total_sum = sum(total)
        if self.__number_items > 10:
            total_sum *= 0.9
        return round(total_sum * 0.1, 2)

    # 7. Общая сумма налога
    # Напиши метод total_tax. Он возвращает общую сумму НДС по чеку.
    def total_tax(self):
        return round(self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation(), 2)

    # 8. Статический метод — номер телефона
    # Напиши статический метод get_telephone_number. Он возвращает номер телефона покупателя.
    # На вход метод принимает аргумент telephone_number. Это десять цифр после +7.
    # Чтобы метод вернул корректный номер, используй в теле условия:
    # - Если передано не целое число, выводится исключение ValueError с текстом 'Необходимо ввести цифры';
    # - Если в аргументе больше 10 символов, выводится исключение ValueError с текстом 'Необходимо ввести 10 цифр после "+7"';
    # - В остальных случаях метод возвращает полный номер телефона.
    # Подсказки
    #   - Чтобы принудительно вызвать исключение, используй оператор raise.
    #   - Чтобы исключение вывело конкретное сообщение, передай текст после имени исключения, в круглых скобках. Например, ValueError('Недопустимое значение').
    #   - Добавить элемент в список можно через append().
    #   - Чтобы удалить элемент из списка, используй remove().
    #   - Посчитать сумму элементов списка поможет функция sum().
    #   - Чтобы выяснить общую сумму НДС, сложи результаты ten_percent_tax_calculation() и twenty_percent_tax_calculation().
    #   - Чтобы вернуть полный номер телефона, используй f-strings. Добавь +7 к аргументу telephone_number.
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        number_str = str(telephone_number)
        if len(number_str) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{number_str}'