from fastapi import FastAPI
from api.endpoints import router as product_router

app = FastAPI()

# Incluir las rutas del producto
app.include_router(product_router)
