from binarysearchtree import Transaction

from prettytable import PrettyTable
def tampilkan_data_transaksi(data_transaksi):
    table = PrettyTable()
    table.field_names = ["Nama Konsumen", "No. SKU barang yang dibeli", "Jumlah Beli", "Subtotal"]
    print("Data Transaksi Konsumen:")
    for transaksi in data_transaksi:
        table.add_row(transaksi)
    print(table)

# Contoh penggunaan dengan perulangan
data_transaksi = Transaction()
data_transaksi.insert(["John Doe", "SKU123", 2, 100])
data_transaksi.insert(["Jane Smith", "SKU456", 3, 150])
data_transaksi.insert(["Michael Johnson", "SKU789", 1, 50])

while True:
    print("Sub Menu Kelola Transaksi Konsumen")
    print("1. Tampilkan Data Transaksi")
    print("2. Keluar")

    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == "1":
        tampilkan_data_transaksi(data_transaksi.findAll())
        input("Tekan Enter untuk melanjutkan...")
    elif pilihan == "2":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

