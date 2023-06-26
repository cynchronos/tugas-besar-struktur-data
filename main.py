import os
import sys
from transaction import tambah_data_transaksi
from displaysubtotal import sort
from stockinput import addStock
from displayalltransaction import tampilkan_data_transaksi
from restock import restok_barang

def main():
    os.system("cls") if sys.platform == 'win32' else os.system("clear")
    print("====================================================")
    print("SISTEM INFORMASI STOK DAN TRANSAKSI")
    print("====================================================")
    menu = ["Kelola Stok Barang","Kelola Transaksi Konsumen","Keluar"]

    for i,menu in enumerate(menu):
        print(i+1,'. ',menu)

    tanyauser = input("Silahkan pilih no menu : ")
    if tanyauser == '1':
        Menu_Kelola_Stok_Barang()
    if tanyauser == '2':
        Menu_Kelola_Transaksi_Konsumen()
    if tanyauser == '3':
        exit

def Menu_Kelola_Stok_Barang():
    os.system("cls") if sys.platform == 'win32' else os.system("clear")
    print("====================================================")
    print("KELOLA STOK BARANG")
    print("====================================================")
    menu2 = ["Input Data Stok Barang","Restok Barang","Kembali","Keluar"]
    for i,menu2 in enumerate(menu2):
        print(i+1,'. ',menu2)
    tanyauser1 =input("Silahkan Pilih no menu : ")
    if tanyauser1 == "1":
        addStock()
        Menu_Kelola_Stok_Barang()
    elif tanyauser1 == "2":
        restok_barang()
        input("Tekan Enter Untuk Keluar")
        Menu_Kelola_Stok_Barang()
    elif tanyauser1 == "3":
        main()
    elif tanyauser1 == "4":
        exit

def Menu_Kelola_Transaksi_Konsumen():
    os.system("cls") if sys.platform == 'win32' else os.system("clear")
    print("====================================================")
    print("KELOLA TRANSAKSI KONSUMEN")
    print("====================================================")
    menu3 = ["Input Data Transaksi Baru","Lihat Data Seluruh Transaksi Konsumen","Lihat Data Transaksi Berdasarkan Subtotal","kembali","Keluar"]
    for i,menu3 in enumerate(menu3):
        print(i+1,'. ',menu3)
    tanyauser2 =input("Silahkan Pilih no menu : ")
    if tanyauser2 == "1":
        tambah_data_transaksi()
        input("Tekan Enter Untuk Keluar")
        Menu_Kelola_Transaksi_Konsumen()
    elif tanyauser2 == "2":
        tampilkan_data_transaksi()
        input("Tekan Enter Untuk Keluar")
        Menu_Kelola_Transaksi_Konsumen()
    elif tanyauser2 == "3":
        sort()
        input("Tekan Enter Untuk Keluar")
        Menu_Kelola_Transaksi_Konsumen()
    elif tanyauser2 == "4":
        main()
    elif tanyauser2 == "5":
        exit
main()