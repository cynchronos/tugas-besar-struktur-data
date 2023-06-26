from prettytable import PrettyTable
from binarysearchtree import Transaction


def sort():
    transactions = Transaction.findAll()
    if transactions is None:
        return print('Data Transaksi Kosong')
    
    for i in range(len(transactions)):
        for j in range(len(transactions) - 1):
            if transactions[j]["subtotal"] < transactions[j + 1]["subtotal"]:
                transactions[j], transactions[j + 1] = (
                    transactions[j + 1],
                    transactions[j],
                )

        table = PrettyTable()
        table.field_names = ["Nama Konsumen", "No SKU", "Jumlah Beli", "Subtotal"]
        for transaction in transactions:
            table.add_row(
                [
                    transaction["nama_konsumen"],
                    transaction["no_sku"],
                    transaction["jumlah_beli"],
                    transaction["subtotal"],
                ]
            )

        return print(table)
