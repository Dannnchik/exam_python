stores = [
    {'id': 1, 'name': 'Asia'},
    {'id': 2, 'name': 'Globus'},
    {'id': 3, 'name': 'Spar'}
]

products = [
    {'name': 'Chocolate', 'category': 'food products', 'price': 11, 'stock': 132, 'store_id': 1 },
    {'name': 'Bread', 'category': 'food products', 'price': 3.0, 'stock': 32, 'store_id': 2},
    {'name': 'Milk', 'category': 'Dairy', 'price': 70, 'stock': 112, 'store_id': 1},
    {'name': 'Eggs', 'category': 'Dairy', 'price': 14, 'stock': 320, 'store_id': 3},
    {'name': 'Coca-Cola', 'category': 'drinks', 'price': 90, 'stock': 3980, 'store_id': 2},
    {'name': 'POP-IT', 'category': 'Toys', 'price': 700, 'stock': 20, 'store_id': 3},
]


def display_stores():
    print("вы можете отобразить список продуктов по выбранному id магазина из")
    print("перечня магазинов ниже, для выхода из программы введите цифру 0:")
    for store in stores:
        print(f"{store['id']}, {store['name']}")

def display_products(store_id):
    print(f"\nПродукты в магазине с id {store_id}:")
    found = False
    for product in products:
        if product['store_id'] == store_id:
            print(f"name of product: {product['name']}")
            print(f"category: {product['category']}")
            print(f"price: {product['price']}")
            print(f"amount in storage: {product['stock']}")
            found = True
        if not found:
            print('продукты не найдены')

def main():
    while True:
        display_stores()
        try:
            store_id = int(input('enter store id (or 0 for exit):'))
            if store_id == 0:
                print('выход из программы')
                break
            elif any(store['id'] == store_id for store in stores):
                display_products(store_id)
            else:
                print("non correct store id! Please, try again")
        except ValueError:
            print("enter correct number")

if __name__ == "__main__":
    main()


