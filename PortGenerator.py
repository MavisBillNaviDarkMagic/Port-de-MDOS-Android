class PortGenerator:
    def __init__(self):
        self.git_manager = GitManager()
        self.port_settings = {
            "templates_enabled": True,
            "auto_adaptation": True,
            "shared_components": ["core", "security", "avatar"]
        }
        
    def generate_new_port(self, target_os):
        """Genera un nuevo port para el sistema operativo especificado"""
        template = self.git_manager.create_port_template(target_os)
        return {
            "port_created": True,
            "os": target_os,
            "structure": template["base_structure"],
            "config": template["specific_configs"]
        }
        
    def adapt_core_components(self, os_type):
        """Adapta los componentes principales para el nuevo OS"""
        return {
            "core_adapted": True,
            "components": self.git_manager.get_base_structure()["core"],
            "os_specific": True
        }
        
    def setup_repository(self, port_name):
        """Configura el repositorio para el nuevo port"""
        return {
            "repo_name": f"Port-de-MDOS-{port_name}",
            "structure": "initialized",
            "git_ready": True
        }