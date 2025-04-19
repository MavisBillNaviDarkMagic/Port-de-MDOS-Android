class HelpSystem:
    def __init__(self):
        self.ayuda_basica = {
            "inicio": {
                "titulo": "Bienvenido a MDOS",
                "pasos": [
                    "Toca el botón grande con el engranaje ⚙️ para configurar",
                    "Usa el botón con el signo ? para obtener ayuda",
                    "Desliza los controles para ajustar"
                ]
            },
            "configuracion": {
                "pantalla": "Mueve el control para ajustar el brillo",
                "sonido": "Toca los botones para cambiar el volumen",
                "accesibilidad": "Elige el tamaño de letra que prefieras"
            },
            "ayuda_rapida": {
                "problemas": "Toca el botón azul de ayuda",
                "dudas": "Pregunta al asistente de voz",
                "cambios": "Usa los botones grandes para cambiar opciones"
            }
        }
        
    def mostrar_ayuda(self, seccion):
        return {
            "tipo": "ayuda_visual",
            "contenido": self.ayuda_basica[seccion],
            "asistente_voz": True
        }
        
    def guia_paso_a_paso(self, accion):
        guias = {
            "configurar": ["Toca el botón de configuración",
                         "Elige qué quieres cambiar",
                         "Mueve los controles hasta que te guste"],
            "personalizar": ["Selecciona tu perfil",
                           "Ajusta el tamaño de letra",
                           "Elige los colores que prefieras"]
        }
        return {
            "pasos": guias[accion],
            "animaciones": True,
            "voz_guia": True
        }