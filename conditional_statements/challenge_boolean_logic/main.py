seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100
# define boolean variable - overstock_risk
overstock_risk = seasonal and (current_stock >= high_stock_threshold)
# define boolean variable - discount_eligible
discount_eligible = not selling_well and not on_sale
# create boolean variable - make_discount
make_discount = overstock_risk or discount_eligible

print("Should the item be discounted?", make_discount)
