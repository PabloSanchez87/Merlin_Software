from project.logic.calculate_score import calculate_score

# Pruebas para la función calculate_score

def test_calculate_score():
    """
    Prueba para la función calculate_score con valores válidos.
    Verifica que la puntuación se calcule correctamente según los pesos y valores proporcionados.
    """
    sales_weight = 0.7
    stock_weight = 0.3
    sales_value = 100000
    stock_value = 50000
    expected_score = (sales_weight * sales_value) + (stock_weight * stock_value)
    assert calculate_score(sales_weight, stock_weight, sales_value, stock_value) == expected_score


def test_calculate_score_zero_values():
    """
    Prueba para la función calculate_score con valores de ventas y stock iguales a 0.
    Verifica que la puntuación calculada sea 0.
    """
    sales_weight = 0.5
    stock_weight = 0.5
    sales_value = 0
    stock_value = 0
    expected_score = 0
    assert calculate_score(sales_weight, stock_weight, sales_value, stock_value) == expected_score
    
