from binarysearchtree import Transaction

from prettytable import PrettyTable

def tampilkan_data_transaksi():
    transaksi = Transaction.findAll()  
    table = PrettyTable()
    table.field_names = ["Nama Konsumen", "No. SKU barang yang dibeli", "Jumlah Beli", "Subtotal"]
    print("Data Transaksi Konsumen:")
    for transaksi in transaksi:
        table.add_row([
        transaksi["nama_konsumen"],
        transaksi["no_sku"],
        transaksi["jumlah_beli"],
        transaksi["subtotal"],
        ])
    print(table)