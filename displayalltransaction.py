from binarysearchtree import Transaction

from prettytable import PrettyTable
def tampilkan_data_transaksi(data_transaksi):
    table = PrettyTable()
    table.field_names = ["Nama Konsumen", "No. SKU barang yang dibeli", "Jumlah Beli", "Subtotal"]
    print("Data Transaksi Konsumen:")
    for transaksi in data_transaksi:
        table.add_row(transaksi)
    print(table)
