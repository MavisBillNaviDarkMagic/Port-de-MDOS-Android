class SimpleInterface:
    def __init__(self):
        self.safe_settings = SafeSettings()
        self.visual_helper = VisualHelper()
        
        self.botones_principales = {
            "ajustes": {
                "icono": "⚙️",
                "tamaño": "extra_grande",
                "color": "azul_suave"
            },
            "ayuda": {
                "icono": "❓",
                "tamaño": "extra_grande",
                "color": "verde_suave"
            },
            "volver": {
                "icono": "⬅️",
                "tamaño": "grande",
                "color": "gris_suave"
            }
        }
        
    def mostrar_menu_principal(self, tipo_usuario):
        return {
            "titulo": "¿Qué quieres hacer?",
            "botones": self.botones_principales,
            "ayuda": self.visual_helper.mostrar_ayuda(tipo_usuario, "inicio"),
            "voz_activa": True
        }
        
    def configurar_ajuste(self, categoria, opcion):
        opciones = self.safe_settings.settings_categories[categoria][opcion]
        return {
            "tipo": "selector_simple",
            "opciones": opciones,
            "ayuda_visual": True,
            "confirmacion": "¿Te gusta así?"
        }
        
    def mostrar_ayuda_contextual(self, seccion):
        return self.visual_helper.mostrar_ayuda("principiante", seccion)