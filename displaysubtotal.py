from prettytable import PrettyTable
from binarysearchtree import Transaction


class DisplaySubtotal:
    def sort(self, transaction):
        # bubble sort in ascending transaction subtotal bst
        for i in range(len(transaction)):
            for j in range(len(transaction) - 1):
                if transaction[j]["subtotal"] < transaction[j + 1]["subtotal"]:
                    transaction[j], transaction[j + 1] = (
                        transaction[j + 1],
                        transaction[j],
                    )

        return transaction


array = [
    {"nama_konsumen": "Dodo", "no_sku": "0001", "jumlah_beli": 2, "subtotal": 20000},
    {"nama_konsumen": "Mahmud", "no_sku": "0003", "jumlah_beli": 3, "subtotal": 15000},
    {"nama_konsumen": "Zeta", "no_sku": "0002", "jumlah_beli": 4, "subtotal": 40000},
    {
        "nama_konsumen": "Arona",
        "no_sku": "SUBA0025",
        "jumlah_beli": 3,
        "subtotal": 32000,
    },
]

Transaction.insertMany(array)

transactions = DisplaySubtotal().sort(Transaction.findAll())
table = PrettyTable()
table.field_names = ["Nama Konsumen", "No SKU", "Jumlah Beli", "Subtotal"]
for transaction in transactions:
    table.add_row(
        [
            transaction["nama_konsumen"],
            transaction["no_sku"],
            transaction["jumlah_beli"],
            transaction["subtotal"],
        ]
    )

print(f'Order Sort: {transaction}')
print(table)

# Stock.insert(
#     {"no_sku": "0001", "nama_barang": "Roti Tawar", "harga": 10000, "jumlah_stock": 10}
# )

#! PERLU DIPAHAMI!!
# sku = input("Masukkan Nomor SKU: ")

# stock_data = Stock.findOne("no_sku", sku)

# if stock_data is not None:
#     print(stock_data)
#     jumlah_stock = int(input("Masukkan jumlah stock: "))
#     new_stock = stock_data["jumlah_stock"] + jumlah_stock
#     result = Stock.update(
#         "no_sku", stock_data["no_sku"], {"nama_barang": "Roti Jahe", "jumlah_stock": new_stock}
#     )
#     print("Update stok sukses") if result == True else print("Gagal update stock")
#     print(Stock.findOne("no_sku", "0001"))
# else:
#     print("Stok tidak ditemukan")
