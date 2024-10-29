from fastapi import APIRouter, HTTPException
from schemas.product_schemas import SortProductsRequest
from logic.calculate_score import calculate_score

router = APIRouter()

@router.get("/")
async def read_root():
    return {
        "Merlin Software": "Bienvenido a la API de Ordenación de Productos",
        "context": "Sistemas que automatice la ordenación de productos",
        "version": "1.0.0",
        "endpoints": [
            "/sort-products - Ordena los productos automáticamente según ventas y stock.",
            "/docs - Documentación de la API en formato OpenAPI.",
            "/redoc - Documentación de la API en formato HTML.",
        ],
        "contact": {
            "developer": "Pablo Sánchez",
            "email": "sancheztorrespablo@gmail.com",   
        },
        "note": "Merlin Software -- Candidatura Junior Software Engineer.",
    }
    
@router.post("/sort-products")
async def sort_products(request: SortProductsRequest):
    try:
        # Convertir las listas de ventas y stock en diccionarios para un acceso más fácil
        sales_dict = {item.productId: item.sales for item in request.productSales}
        stock_dict = {item.productId: item.stock for item in request.productStock}

        # Crear una lista de productos con sus puntuaciones calculadas
        products = []
        for product_id in sales_dict:
            if product_id in stock_dict:
                # Lógica de priorización: calcular la puntuación del producto
                score = calculate_score(
                    request.salesWeight,
                    request.stockWeight,
                    sales_dict[product_id],
                    stock_dict[product_id]
                )
                products.append({"productId": product_id, "score": score})

        # Ordenar los productos por puntuación en orden descendente
        sorted_products = sorted(products, key=lambda x: x["score"], reverse=True)

        # Devolver solo los identificadores de los productos en el orden calculado
        sorted_product_ids = [product["productId"] for product in sorted_products]

        return sorted_product_ids

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")
