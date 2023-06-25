import os

def main():
    os.system("cls")
    print("====================================================")
    print("SISTEM INFORMASI STOK DAN TRANSAKSI")
    print("====================================================")
    menu = ["1.Kelola Stok Barang","2.Kelola Transaksi Konsumen",]

    for i,menu in enumerate(menu):
        print(i+1,'. ',menu)

    global tanyauser
    tanyauser = input("Silahkan pilih no menu : ")

def pilihan():
    if tanyauser == '1':
        print("====================================================")
        print("KELOLA STOK BARANG")
        print("====================================================")
        menu2 = ["1.Input Data Stok Barang","2.Restok Barang"]
        for i,menu2 in enumerate(menu2):
            print(i+1,'. ',menu2)
        tanyauser1 =input("Silahkan Pilih no menu : ")
        if tanyauser1 == "1":
            print("lanjut ke prgram input data stok barang")
        elif tanyauser1 == "2":
            print("lanjut ke program restok barang")

    elif tanyauser == "2":
        print("====================================================")
        print("KELOLA Transaksi Konsumen")
        print("====================================================")
        menu2 = ["1.Input Data Transaksi Baru","2.Lihat Data Seluruh Transaksi Konsumen","3"]
        for i,menu2 in enumerate(menu2):
            print(i+1,'. ',menu2)
        tanyauser1 =input("Silahkan Pilih no menu : ")
