# This program let user to input the product and price in the list.
products = []
while True:
    name = input('Please type the product name or type "q" to quit: ')
    if name == 'q':
        break
    price = input('Please type the product price: ')
    # way3，Best solution!
    products.append([name, price])

print(products)
print('The first product name is ', products[0][0])