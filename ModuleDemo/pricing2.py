from pricing import get_net_price

price = 150
tax_rate = 0.1
discount = 10

net_price = get_net_price(
    price,
    tax_rate,
    discount

)

print(net_price)