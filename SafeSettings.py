class SafeSettings:
    def __init__(self):
        self.settings_categories = {
            "pantalla": {
                "brillo": ["bajo", "medio", "alto"],
                "tamaño_letra": ["pequeño", "normal", "grande", "muy grande"],
                "modo": ["día", "noche", "automático"]
            },
            "sonido": {
                "volumen": ["silencio", "bajo", "medio", "alto"],
                "notificaciones": ["on", "off"],
                "modo": ["normal", "silencio", "vibración"]
            },
            "seguridad": {
                "control_parental": ["on", "off"],
                "apps_permitidas": ["todas", "solo seguras"],
                "modo_niños": ["on", "off"]
            },
            "accesibilidad": {
                "lector_voz": ["on", "off"],
                "contraste": ["normal", "alto"],
                "velocidad_toques": ["normal", "lenta"]
            }
        }
        
    def aplicar_configuracion(self, categoria, opcion, valor):
        if valor in self.settings_categories[categoria][opcion]:
            return {
                "estado": "aplicado",
                "mensaje": "Configuración actualizada correctamente",
                "ayuda": self.obtener_ayuda(categoria, opcion)
            }
        return {
            "estado": "error",
            "mensaje": "Por favor selecciona una opción válida",
            "opciones": self.settings_categories[categoria][opcion]
        }
        
    def obtener_ayuda(self, categoria, opcion):
        ayudas = {
            "pantalla": {
                "brillo": "Ajusta el brillo de la pantalla para ver mejor",
                "tamaño_letra": "Cambia el tamaño del texto para leer más fácil",
                "modo": "Modo día para luz solar, noche para oscuridad"
            },
            "sonido": {
                "volumen": "Controla el volumen general del dispositivo",
                "notificaciones": "Activa o desactiva los avisos",
                "modo": "Elige cómo quieres recibir alertas"
            }
        }
        return ayudas.get(categoria, {}).get(opcion, "¿Necesitas ayuda? Toca aquí")