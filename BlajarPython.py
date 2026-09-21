class Item:
    # class untuk merepresentasikan data sebuah barang
    def __init__(self, name, price, quantity):
        # menyimpan nama, harga, dan jumlah barang
        self.name = name
        self.price = price
        self.quantity = quantity

    # method untuk menampilkan informasi barang
    def display_info(self):
        print(f"Nama Barang: {self.name}")
        print(f"Harga: Rp{self.price:,}")
        print(f"Jumlah: {self.quantity}")


class Inventory:
    # class untuk mengelola data barang dalam inventaris
    def __init__(self, name):
        self.name = name

        # private attribute untuk menyimpan kumpulan object Item
        self.__items = []

    # method untuk menambahkan item ke dalam list
    def add_item(self, item):

        # validasi object harus merupakan instance dari Item
        if isinstance(item, Item):

            # jika valid, item dimasukkan ke private list
            self.__items.append(item)

            print(f"{item.name} berhasil ditambahkan.")

        # jika bukan object Item
        else:
            print("Object yang dimasukkan bukan Item!")

    # private method untuk menghitung total nilai inventaris
    def __calculate_inventory_value(self):

        # variabel awal untuk menyimpan total nilai
        total = 0

        # mengambil setiap item dari private list
        for item in self.__items:

            # harga dikalikan dengan jumlah barang
            total += item.price * item.quantity

        # mengembalikan total nilai inventaris
        return total

    # method untuk menampilkan seluruh data barang
    def show_items(self):

        print(f"\nDaftar Inventaris {self.name}")
        print("---------------------------")

        # menampilkan informasi setiap item
        for item in self.__items:
            item.display_info()
            print("---------------------------")

        # memanggil private method untuk menghitung total nilai inventaris
        print(
            f"Total Nilai Inventaris: "
            f"Rp{self.__calculate_inventory_value():,}"
        )


# membuat object Item
item1 = Item("Laptop", 8000000, 2)
item2 = Item("Keyboard", 500000, 5)
item3 = Item("Mouse", 250000, 10)


# membuat object Inventory
inventory = Inventory("Inventaris Laboratorium")


# menambahkan setiap object Item ke dalam Inventory
inventory.add_item(item1)
inventory.add_item(item2)
inventory.add_item(item3)


# pengujian validasi dengan memasukkan object yang bukan Item
inventory.add_item("Buku")


# menampilkan seluruh data barang dan total nilai inventaris
inventory.show_items()