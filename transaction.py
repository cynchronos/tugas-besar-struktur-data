from binarysearchtree import Transaction,Stock

Stock.insert({"no_sku" : 5521,
            "nama_barang" : "susu",
            "harga_satuan" : 1500,
            "jumlah_stok": 4
})

def tambah_data_transaksi():
    nama_konsumen = input("Masukkan Nama Konsumen: ")
    transaksi = []
    loop = True
    while loop:
        sku = int(input("Masukkan No. SKU barang yang dibeli: "))
        jumlah_beli = int(input("Masukkan Jumlah Beli: "))

        node = Stock.findOne('no_sku', sku)

        if node:
            if node['jumlah_stok'] >= jumlah_beli:
                subtotal = node['harga_satuan'] * jumlah_beli
                node['jumlah_stok'] -= jumlah_beli
                Transaction.insert({
                    "nama_konsumen": nama_konsumen,
                    "no_sku": sku,
                    "jumlah_beli": jumlah_beli,
                    "subtotal": subtotal
                })
                Stock.update('no_sku', sku, node)
                print("Data Transaksi Konsumen Berhasil Diinputkan")
                print(Stock.findOne("no_sku", 5521))
                lanjut = input("Apakah ingin menambahkan data pembelian untuk konsumen ini (Y/N)? ")
                if lanjut.upper() == 'N':
                    loop = False  # Keluar dari loop saat input "N"
            else:
                print("Jumlah Stok No. SKU yang Anda beli tidak mencukupi")
                lanjut = input("Apakah ingin melanjutkan transaksi (Y/N)? ")
                if lanjut.upper() == 'N':
                    break  # Keluar dari loop saat input "N"
        else:
            print("No. SKU yang diinputkan belum terdaftar")
            lanjut = input("Apakah ingin melanjutkan transaksi (Y/N)? ")
            if lanjut.upper() == 'N':
                break  # Keluar dari loop saat input "N"

    return transaksi

