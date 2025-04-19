#!/bin/bash

echo "Iniciando MDOS con verificación de identidad..."

# Verificar Python3
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 no encontrado"
    exit 1
fi

# Iniciar sistema
echo "Iniciando verificación de identidad..."
python3 installer.py

if [ $? -eq 0 ]; then
    echo "Identidad verificada: Christ David Alucard"
    echo "Cuentas vinculadas: Google, Microsoft"
    echo "Estado: Sistema activado"
else
    echo "Error: Verificación fallida"
    exit 1
fi

# Comprobar requisitos
if ! command -v gradle &> /dev/null; then
    echo "Error: Gradle no encontrado"
    exit 1
fi

# Preparar entorno
chmod +x main.py
mkdir -p build/outputs

# Construir proyecto
echo "Construyendo proyecto..."
gradle build

# Iniciar sistema MDOS
echo "Iniciando MDOS..."
python3 main.py

echo "MDOS Android está listo para usar"