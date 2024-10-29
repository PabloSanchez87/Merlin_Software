#!/bin/bash

# Test para la API /sort-products con datos válidos
curl -X POST 'http://127.0.0.1:8080/sort-products' -H 'Content-Type: application/json' -d '{
  "salesWeight": 0.5,
  "stockWeight": 0.5,
  "productSales": [
    {"productId": "1", "sales": 50000},
    {"productId": "2", "sales": 100000},
    {"productId": "3", "sales": 100000},
    {"productId": "4", "sales": 75000}
  ],
  "productStock": [
    {"productId": "1", "stock": 100000},
    {"productId": "2", "stock": 400000},
    {"productId": "3", "stock": 200000},
    {"productId": "4", "stock": 300000}
  ]
}'

echo "\n"

# Test para la API /sort-products con un producto sin stock
curl -X POST 'http://127.0.0.1:8080/sort-products' -H 'Content-Type: application/json' -d '{
  "salesWeight": 0.5,
  "stockWeight": 0.5,
  "productSales": [
    {"productId": "1", "sales": 50000},
    {"productId": "2", "sales": 100000}
  ],
  "productStock": [
    {"productId": "1", "stock": 100000}
  ]
}'

echo "\n"

# Test para la API /sort-products con valores inválidos en salesWeight
curl -X POST 'http://127.0.0.1:8080/sort-products' -H 'Content-Type: application/json' -d '{
  "salesWeight": 1.5,
  "stockWeight": 0.5,
  "productSales": [
    {"productId": "1", "sales": 50000}
  ],
  "productStock": [
    {"productId": "1", "stock": 100000}
  ]
}'

echo "\n"