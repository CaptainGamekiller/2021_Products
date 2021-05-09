import os

# Read the file
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if 'Product, Price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# Prompt the user and get inputs
def user_input(products):
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
    return products

# Print products and price
def print_products(products):
    for p in products:
        print('The price of ', p[0], 'is ', p[1] )

# Write to the .csv file
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('Product, Price \n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'Products.csv'
    if os.path.isfile(filename):  # check the file is existed or not.
        print('This file is existed!')
        products = read_file(filename)
    else:
        print('This file is not existed!')
    products = user_input(products)
    write_file('Products.csv', products)

main()