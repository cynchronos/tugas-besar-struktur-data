from prettytable import PrettyTable
from binarysearchtree import Transaction

class DisplaySubtotal:
  
    def sort(self, transaction):
      # bubble sort in ascending transaction subtotal bst
      for i in range(len(transaction)):
        for j in range(len(transaction)-1):
          if transaction[j]['subtotal'] < transaction[j+1]['subtotal']:
            transaction[j], transaction[j+1] = transaction[j+1], transaction[j]
      
      return transaction
      
  
array = [
  {'nama_konsumen': 'Dodo', 'no_sku': '0001', 'jumlah_beli': 2, 'subtotal': 20000},
  {'nama_konsumen': 'Mahmud', 'no_sku': '0003', 'jumlah_beli': 3, 'subtotal': 15000},
  {'nama_konsumen': 'Zeta', 'no_sku': '0002', 'jumlah_beli': 4, 'subtotal': 40000},
  {'nama_konsumen': 'Arona', 'no_sku': 'SUBA0025', 'jumlah_beli': 3, 'subtotal': 32000}
]

data = Transaction()
data.insertMany(array)

transactions = DisplaySubtotal().sort(data.findAll())
table = PrettyTable()
table.field_names = ['Nama Konsumen', 'No SKU', 'Jumlah Beli', 'Subtotal']
for transaction in transactions:
    table.add_row([transaction['nama_konsumen'], transaction['no_sku'], transaction['jumlah_beli'], transaction['subtotal']])

print(f'Order Sort: {transaction}')
print(table)