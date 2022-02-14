# №5
price_of_products = [57.6, 45.5, 55, 34, 123, 43.64, 100, 100.45, 32.02, 11, 43]
new_list = []
def_zero = 0
for i in price_of_products:
    if price_of_products[def_zero]:
        difference = (price_of_products[def_zero] - int(price_of_products[def_zero])) * 100
        double = f'{int(difference):02}'
        new_list.append(str(int(price_of_products[def_zero])) + " руб " + str(double) + " коп ")
        def_zero += 1
    else:
        new_list.append(price_of_products[def_zero])
        def_zero += 1

sort_list = ', '.join(new_list)
print(sort_list)
same_id = id(price_of_products)
price_of_products.sort()
print(price_of_products)
print(id(price_of_products) == same_id)
my_list = sorted(price_of_products, reverse=True)
print(sorted(my_list[:5]))