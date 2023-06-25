from binarysearchtree import Stock


class InputStock:

    def __init__(self):
        self.array = []

    def addNewInput(self, skuNumber, productName, price, stock):
        stok = Stock.findOne('no_sku', skuNumber)
        if stok :
            return print("Ditolak, duplikat nomor sku terdeteksi")



        inputObject = {
                "no_sku": skuNumber,
                "nama_barang": productName,
                "harga_satuan": price,
                "jumlah_stok": stock
            }
        self.array.append(inputObject)

        for items in self.array:
                Stock.insert(items)
                
        return print(self.array)


def addStock():
    newInput = InputStock()

    while True:
        inputSku = input("masukkan nomor sku: ")
        inputProduct = input("masukkan nama produk: ")
        inputPrice = int(input("masukkan harga produk: "))
        inputStock = int(input("masukkan jumlah stok: "))

        newInput.addNewInput(inputSku, inputProduct, inputPrice, inputStock)

        choice = input("Input Stok Lain? ?   [Y/N]")

        if choice != "Y" and choice != "y":
            break
