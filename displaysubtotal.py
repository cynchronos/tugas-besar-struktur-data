from binarysearchtree import Stock, Transaction

class DisplaySubtotal:
  
    def sort(self, transaction):
      # bubble sort in ascending transaction subtotal bst
      for i in range(len(transaction)):
        for j in range(len(transaction)-1):
          if transaction[j]['subtotal'] < transaction[j+1]['subtotal']:
            transaction[j], transaction[j+1] = transaction[j+1], transaction[j]
      
      return transaction
      
    

data = Transaction()
data.insert({'nama_konsumen': 'Dodo', 'no_sku': '0001', 'jumlah_beli': 2, 'subtotal': 20000})
data.insert({'nama_konsumen': 'Zeta', 'no_sku': '0002', 'jumlah_beli': 4, 'subtotal': 40000})
data.insert({'nama_konsumen': 'Mahmud', 'no_sku': '0003', 'jumlah_beli': 3, 'subtotal': 15000})
data.insert({'nama_konsumen': 'Arona', 'no_sku': '0025', 'jumlah_beli': 3, 'subtotal': 32000})


transaction = DisplaySubtotal().sort(data.findAll())

print(f'Order Sort: {transaction}')