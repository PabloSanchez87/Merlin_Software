```bash
curl -X POST 'http://localhost:8080/sort-products' -H 'Content-Type: application/json' -d '{
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
```

```bash
curl -X POST 'http://localhost:8080/sort-products' -H 'Content-Type: application/json' -d '{
  "salesWeight": 0.9,
  "stockWeight": 0.1,
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
```

```bash
curl -X POST 'http://127.0.0.1:8080/sort-products' -H 'Content-Type: application/json' -d '{
  "salesWeight": 0.7,
  "stockWeight": 0.3,
  "productSales": [
    {"productId": "A", "sales": 25000},
    {"productId": "B", "sales": 150000},
    {"productId": "C", "sales": 30000},
    {"productId": "D", "sales": 5000}
  ],
  "productStock": [
    {"productId": "A", "stock": 20000},
    {"productId": "B", "stock": 5000},
    {"productId": "C", "stock": 15000},
    {"productId": "D", "stock": 30000}
  ]
}'
```	