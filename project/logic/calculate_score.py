def calculate_score(sales_weight, stock_weight, sales_value, stock_value):
    sales_score = sales_weight * sales_value
    stock_score = stock_weight * stock_value
    return sales_score + stock_score
