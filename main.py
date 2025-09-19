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
        average = total/len(sales_totals)
        if sales_totals == {}:
            filtered = {}
        elif q_price > average:
            filtered[candy] = value
        
    return filtered


    
def ninety_nine_bottles(count, beverage):
    poem = []
    for cnt in range(1, count + 1):
        if cnt[0] < cnt[0+1]:

        if cnt == 1:
            poem.append(f"{cnt} bottle of {beverage} on the wall, {cnt} bottle of {beverage}")
            poem.append(f"If one of those bottles should happen to fall, {cnt - 1} bottles of pop on the wall")
        elif cnt > 1:
            poem.append(f"{cnt} bottles of {beverage} on the wall, {cnt} bottles of {beverage},")
            poem.append(f"If one of those bottles should happen to fall, {cnt - 1} bottles of pop on the wall")
    

    return poem      
               
        


