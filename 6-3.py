class Nigiri:
    category = "まぐろ"
    top = "ねた"
    base = "にぎり"

    def show_attributes(self):
        print("top: {}, base: {}, category: {}".format(self.top, self.base, self.category))


class Maguro(Nigiri):
    top = "まぐろ"
    price = 100

    def show_attributes(self):
        super().show_attributes()

    def show_one_dish_price(self, num_nigiri=2):
        result = self.price * num_nigiri
        print("１皿({}かん)の値段: {}円".format(num_nigiri, result))

m5 = Maguro()
m5.show_attributes()
m5.show_one_dish_price()
