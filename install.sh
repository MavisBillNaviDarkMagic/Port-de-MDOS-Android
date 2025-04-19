#!/bin/bash

echo "=== Instalador MDOS Android ==="
echo "Iniciando instalación optimizada..."

# Verificar entorno
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 es necesario"
    exit 1
fi

# Crear directorios necesarios
mkdir -p build/release
mkdir -p quantum_cache
mkdir -p backups

# Ejecutar optimización final
echo "Optimizando sistema..."
python3 final_package.py

# Generar APK
echo "Generando APK..."
./gradlew assembleRelease

# Verificar instalación
echo "Verificando instalación..."
python3 -c "
from UltimateOptimizer import UltimateOptimizer
optimizer = UltimateOptimizer()
status = optimizer.finalize_optimization()
print(f'Estado de optimización: {status[\"status\"]}')
"

echo "¡Instalación completada!"
echo "El APK está listo en build/release/mdos_android.apk"