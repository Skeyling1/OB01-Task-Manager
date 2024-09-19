# программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как адрес, название и ассортимент товаров.
# Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов

class Store:
    def __init__(self, name, address, items):
        self.name = name
        self. address =  address
        self.items = items

    def add_item(self, new_item):
        self.items.update(new_item)

    def del_item(self, item_to_del):
        self.items.pop(item_to_del)

    def price(self, item_to_price):
        print(self.items.get(item_to_price)) #получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.

    def renew_price(self, new_item):
        self.items.update(new_item)

shop1 = Store("игрушки", "Сыктывкар", {'кукла':88, 'заяц':71, 'еж':11})

shop2 = Store("продукты", "Москва", {'сыр':885, 'джем':731, 'сок':121})

shop3 = Store("спорт", "Казань", {'лыжи':777, 'ласты':555, 'мяч':444})

shop2.add_item({'морская капуста':3333333333})
print(shop2.items)

shop2.del_item('морская капуста')
print(shop2.items)

shop2.price('сыр')

shop2.renew_price({'сыр':9999})
print(shop2.items)
