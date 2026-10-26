import os

discount = 0.1
 
 
def read_orders(filename):
    global total_price
    orders = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            orders.append(parts)
    return orders
 
 
def calculate_total(orders):
    total_price = 0
    for order in orders:
        price = float(order[1])
        qty = int(order[2])
        total_price += price * qty
    if total_price > 1000:
        total_price = total_price * (1 - discount)
    return total_price
 
 
def print_report(orders, total):
    print('Order Report')
    for order in orders:
        print(order[0], order[1], order[2])
    print('Total:', total)
 
 
def log_to_file(total):
    with open('log.txt', 'a') as f:
        f.write(str(total) + '\n')
 
 
def main():
    orders = read_orders('orders.csv')
    total = calculate_total(orders)
    print_report(orders, total)
    log_to_file(total)
 
 
if __name__ == '__main__':
    main()
