def calculate_score(sales_weight, stock_weight, sales_value, stock_value):
    try:
        sales_score = sales_weight * sales_value
        stock_score = stock_weight * stock_value
        return sales_score + stock_score
    except Exception as e:
        raise ValueError(f"Error al calcular la puntuación del producto: {e}")
