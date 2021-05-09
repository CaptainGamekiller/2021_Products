# This program let user to input the product and price in the list.
import os # operating system

# Read the file
products = []
if os.path.isfile('Products.csv'): # check the file is existed or not.
    print('This file is existed!')
    with open('Products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if 'Product, Price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print('Those products are in the file: ', products)
else:
    print('This file is not existed!')

# Prompt the user and get inputs
while True:
    print('--------------------------------------------------------------')
    name = input('Please type the product name or type "q" to quit: ')
    if name == 'q':
        break
    price = input('Please type the product price: ')
    price = int(price)
    products.append([name, price])
print('Update the file!')
print('New products and price are showing below: \n', products)

# write to the .csv file
with open ('Products.csv', 'w', encoding = 'utf-8') as f:
    f.write('Product, Price \n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')