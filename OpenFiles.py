sale = open("sales.txt", "r")

for sales in sale.readlines():
    print(sales)
sale.close()