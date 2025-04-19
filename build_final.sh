#!/bin/bash

echo "Iniciando compilación final de MDOS Android..."

# Verificar entorno
python3 -c "from FinalBuilder import FinalBuilder; builder = FinalBuilder()"
if [ $? -ne 0 ]; then
    echo "Error: Entorno no preparado"
    exit 1
fi

# Compilar APK
echo "Compilando APK..."
./gradlew assembleRelease

# Optimizar y verificar
python3 -c "
from FinalBuilder import FinalBuilder
builder = FinalBuilder()
builder.compile_final_package()
builder.verify_package_integrity()
print('APK generado y verificado correctamente')
"

echo "MDOS Android está listo para instalar"
echo "Ubicación del APK: build/outputs/apk/release/mdos_android.apk"