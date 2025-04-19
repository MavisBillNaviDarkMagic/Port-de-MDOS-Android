class VisualHelper:
    def __init__(self):
        self.tutorial_mode = True
        self.animation_enabled = True
        self.visual_guides = {
            "principiante": {
                "mensajes": "grandes",
                "animaciones": "lentas",
                "instrucciones": "paso_a_paso"
            },
            "mayor": {
                "contraste": "alto",
                "sonido": "fuerte",
                "velocidad": "muy_lenta"
            },
            "niño": {
                "colores": "vivos",
                "iconos": "grandes",
                "efectos": "divertidos"
            }
        }
        
    def mostrar_ayuda(self, tipo_usuario, seccion):
        return {
            "tipo": "ayuda_visual",
            "estilo": self.visual_guides[tipo_usuario],
            "animacion": self.generar_tutorial(seccion)
        }
        
    def generar_tutorial(self, seccion):
        tutoriales = {
            "inicio": "Toca los iconos grandes para elegir lo que quieres hacer",
            "ajustes": "Desliza los botones para cambiar como funciona",
            "ayuda": "¡Toca el botón azul grande si necesitas más ayuda!"
        }
        return {
            "mensaje": tutoriales[seccion],
            "video_guia": True,
            "asistente_voz": True
        }
        
    def asistente_vocal(self, mensaje):
        return {
            "voz": "amigable",
            "velocidad": "lenta",
            "repetir": True
        }