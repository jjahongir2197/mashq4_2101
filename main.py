class Item:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty

    def add(self, amount):
        self.qty += amount

    def remove(self, amount):
        if amount > self.qty:
            print("Yetarli emas")
        else:
            self.qty -= amount


class Warehouse:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show(self):
        for i in self.items:
            print(i.name, i.qty)


wh = Warehouse()

while True:
    print("\n1. Mahsulot qo‘shish")
    print("2. Kirim")
    print("3. Chiqim")
    print("4. Ombor")
    print("0. Chiqish")

    c = input(">>> ")

    if c == "1":
        wh.add_item(Item(input("Nomi: "), int(input("Soni: "))))

    elif c == "2":
        n = input("Nomi: ")
        for i in wh.items:
            if i.name == n:
                i.add(int(input("Miqdor: ")))

    elif c == "3":
        n = input("Nomi: ")
        for i in wh.items:
            if i.name == n:
                i.remove(int(input("Miqdor: ")))

    elif c == "4":
        wh.show()

    elif c == "0":
        break
