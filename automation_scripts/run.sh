#!/bin/bash

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
fastapi dev main.py --port 8080