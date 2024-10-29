from fastapi.testclient import TestClient
from project.main import app

client = TestClient(app)

# Pruebas para el endpoint '/sort-products'

def test_sort_products_success():
    """
    Prueba para el endpoint '/sort-products' con un caso exitoso.
    Verifica que los productos se ordenen correctamente según las ventas y el stock.
    """
    request_payload = {
        "salesWeight": 0.5,
        "stockWeight": 0.5,
        "productSales": [
            {"productId": "1", "sales": 50000},
            {"productId": "2", "sales": 100000},
            {"productId": "3", "sales": 75000}
        ],
        "productStock": [
            {"productId": "1", "stock": 100000},
            {"productId": "2", "stock": 400000},
            {"productId": "3", "stock": 200000}
        ]
    }
    response = client.post("/sort-products", json=request_payload)
    assert response.status_code == 200
    assert response.json() == ["2", "3", "1"]


def test_sort_products_missing_stock():
    """
    Prueba para el endpoint '/sort-products' donde falta información de stock para un producto.
    Verifica que el endpoint devuelva únicamente los productos con stock disponible.
    """
    request_payload = {
        "salesWeight": 0.5,
        "stockWeight": 0.5,
        "productSales": [
            {"productId": "1", "sales": 50000},
            {"productId": "2", "sales": 100000}
        ],
        "productStock": [
            {"productId": "1", "stock": 100000}
        ]
    }
    response = client.post("/sort-products", json=request_payload)
    assert response.status_code == 200
    assert response.json() == ["1"]


def test_sort_products_invalid_weight():
    """
    Prueba para el endpoint '/sort-products' con un valor inválido para salesWeight.
    Verifica que el endpoint devuelva un error de validación (código de estado 422).
    """
    request_payload = {
        "salesWeight": 1.5,  # Valor inválido
        "stockWeight": 0.5,
        "productSales": [
            {"productId": "1", "sales": 50000}
        ],
        "productStock": [
            {"productId": "1", "stock": 100000}
        ]
    }
    response = client.post("/sort-products", json=request_payload)
    assert response.status_code == 422  # Error de validación
