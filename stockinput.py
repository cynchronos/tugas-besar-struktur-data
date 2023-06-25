from binarysearchtree import Stock


class InputStock:

    def __init__(self):
        self.array = []

    def addNewInput(self, skuNumber, productName, price, stock):
        is_duplicate = False

        if skuNumber == Stock.findOne('no_sku', skuNumber):
          print("Ditolak, duplikat nomor sku terdeteksi")
          is_duplicate = True
          
        if is_duplicate == True:
          print("ditolak, duplikasi sku terdeteksi")

        if is_duplicate == False:
            inputObject = {
                "no_sku": skuNumber,
                "nama_barang": productName,
                "harga_satuan": price,
                "jumlah_stok": stock
            }
            self.array.append(inputObject)

            for items in self.array:
                Stock.insert(items)
                
            print(self.array)


def addStock():
    newInput = InputStock()

    while True:
        inputSku = input("masukkan nomor sku: ")
        inputProduct = input("masukkan nama produk: ")
        inputPrice = int(input("masukkan harga produk: "))
        inputStock = int(input("masukkan jumlah stok: "))

        newInput.addNewInput(inputSku, inputProduct, inputPrice, inputStock)

        choice = input("input another stuff ?   [Y/N]")

        if choice != "Y" and choice != "y":
            break
