# Python Advanced Exam - 18 February 2023

def shop_from_grocery_list(budget, grocery_list, *args):
    bought_products = []
    for product, price in args:
        if product not in bought_products:
            continue
        if budget - (float(price)) < 0:
            break
        else:
            bought_products.append(product)
            grocery_list.remove(product)
            budget -= float(price)
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."