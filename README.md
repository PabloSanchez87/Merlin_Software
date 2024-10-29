# Ordenación Automática de Productos - Merlin Software

## Descripción
Este proyecto es un servicio web que ofrece una API REST para la ordenación automática de productos según ventas recientes y stock disponible. La solución está diseñada para ayudar a la pequeña empresa de venta en línea a automatizar el proceso de clasificación de productos, permitiendo configuraciones personalizadas para maximizar la relevancia de cada producto según la demanda y la disponibilidad.

## Tecnologías Utilizadas
- **Python** (versión 3.12)
- **FastAPI**: Para la creación de la API REST.
- **Pydantic**: Para la validación de esquemas de datos.

He escogido **FastAPI** para este proyecto debido a su eficiencia y simplicidad al crear APIs RESTful. Ofrece validación de datos con **Pydantic**, una sintaxis fácil de usar y una estructura clara para definir rutas y endpoints. Además, ofrece una buena documentación con **Swagger**.

## Estructura del Proyecto
```
Merlin_Software/
  project/
    main.py
    api/
      endpoints.py
    logic/
      calculate_score.py
    schemas/
      product_schemas.py
```
- **main.py**: Archivo principal que arranca la aplicación.
- **api/endpoints.py**: Define los endpoints de la API, incluyendo el endpoint de ordenación de productos (`/sort-products`).
- **logic/calculate_score.py**: Contiene la lógica para calcular la puntuación de cada producto en función de ventas y stock.
- **schemas/product_schemas.py**: Define los esquemas de los datos de productos.

## Instalación y Ejecución

### Prerrequisitos
- Python 3.12
- Pipenv o virtualenv para gestionar el entorno virtual.

### Instalación
1. Clona este repositorio:
   ```sh
   git clone git@github.com:PabloSanchez87/Merlin_Software.git
   cd Merlin_Software
   code . # Opcional, solo si usas VSCode
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac/WSL
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```sh
   fastapi dev main.py --port 8080
   ```
   La API estará disponible en `http://127.0.0.1:8080`.

### `Scripts de Automatización (OPCIONAL)`

En la carpeta `automation_scripts/` se encuentran varios scripts que ayudan a simplificar la configuración y ejecución del proyecto:

- **`run.sh`**: Crea un entorno virtual, instala las dependencias y ejecuta la aplicación. Puedes ejecutarlo con:
  ```sh
  ./automation_scripts/run.sh
  ```

- **`test.sh`**: Ejecuta las pruebas del proyecto usando pytest. Puedes ejecutarlo con:
  ```sh
  ./automation_scripts/test.sh
  ```

- **`test_api.sh`**: Realiza varias solicitudes cURL al endpoint `/sort-products` para probar la funcionalidad de la API. Puedes ejecutarlo con:
  ```sh
  ./automation_scripts/test_api.sh
  ```

### Permisos de Ejecución
Antes de ejecutar estos scripts, asegúrate de darles permisos de ejecución:
```sh
chmod +x automation_scripts/*.sh
```

## Uso de la API

### Endpoint `/sort-products`
- **Método**: `POST`
- **URL**: `/sort-products`
- **Descripción**: Ordena productos según ventas y stock utilizando ponderaciones configurables.
- **Cuerpo de la Petición**:
  ```json
  {
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
  }
  ```
- **Respuesta**:
  - Lista de identificadores de productos ordenados por prioridad (de mayor a menor).
  ```json
    ["2", "4", "3", "1"]   
  ```

## Pruebas
Puedes probar el funcionamiento del endpoint utilizando `cURL`:
```bash
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
```

## Tests

### Ejecución de Tests
El proyecto incluye un conjunto de pruebas unitarias y de integración para verificar el funcionamiento del endpoint `/sort-products` y la función `calculate_score`. Estas pruebas están ubicadas en el directorio `tests/`.

Para ejecutar las pruebas, asegúrate de que el entorno virtual esté activado y ejecuta el siguiente comando desde la raíz del proyecto (`Merlin_Software`):

```sh
pytest -v tests/
```
Esto ejecutará todas las pruebas definidas y proporcionará un resumen de los resultados.

## Consideraciones
- **Configurabilidad**: Puedes modificar las ponderaciones (`salesWeight` y `stockWeight`) para ajustar la prioridad de ventas o stock según tus necesidades.
- **Validación**: La API asegura que todos los productos proporcionados tengan valores tanto de ventas como de stock antes de calcular la puntuación.

## Contacto
- **Desarrollador**: Pablo Sánchez
- **Email**: [sancheztorrespablo@gmail.com](mailto:sancheztorrespablo@gmail.com)

