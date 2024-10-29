from fastapi import FastAPI
from api.endpoints import router as product_router

app = FastAPI(
    title="Ordenación de Productos - Merlin Software",
    description="API para ordenar productos según ventas y stock con ponderaciones configurables.",
    version="1.0.0"
    )

# Incluir las rutas del producto
app.include_router(product_router)
