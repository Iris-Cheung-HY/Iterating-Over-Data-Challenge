def calculate_total_sales(sales_totals):
    total = 0
    for candy, value in sales_totals.items():
        q_price = value["quantity"] * value["price"]
        total += q_price
    return total

def calculate_average_sales(sales_totals):
    total = 0
    for candy, value in sales_totals.items():
        q_price = value["quantity"] * value["price"]
        total += q_price
    if sales_totals == {}:
        average = 0.0
    else:
        average = total/len(sales_totals)
    return average 
    

def filter_to_better_than_average_sales(sales_totals):
    filtered = {}
    total = 0
    for candy, value in sales_totals.items():
        q_price = value["quantity"] * value["price"]
        total += q_price
    if sales_totals == {}:
        average = 0.0
    else:
        average = total/len(sales_totals)
    
    if q_price > average:
        filtered.append(candy)
        


    
def ninety_nine_bottles(count, beverage):
    pass
