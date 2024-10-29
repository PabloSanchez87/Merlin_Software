from pydantic import BaseModel, Field
from typing import List

class ProductSales(BaseModel):
    productId: str
    sales: float

class ProductStock(BaseModel):
    productId: str
    stock: int

class SortProductsRequest(BaseModel):
    salesWeight: float = Field(..., gt=0, le=1, description="Ponderación para las ventas (entre 0 y 1)")
    stockWeight: float = Field(..., gt=0, le=1, description="Ponderación para el stock (entre 0 y 1)")
    productSales: List[ProductSales]
    productStock: List[ProductStock]
