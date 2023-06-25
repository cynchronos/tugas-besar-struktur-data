class InputStock:

  def __init__(self):
    self.array = []

  def addNewInput(self, skuNumber, productName, price, stock):
    is_duplicate = False
    for sku in self.array:
      if skuNumber == sku[0]:
        print("rejected, sku duplication detected")
        is_duplicate = True
        break

    if is_duplicate == False:
      inputObject = [skuNumber, productName, price, stock]
      self.array.append(inputObject)
      print(self.array)


def main():
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


main()
