class GitManager:
    def __init__(self):
        self.repo_config = {
            "main_repo": "MDOS-Android",
            "ports": {
                "android": "/Port-de-MDOS-Android",
                "ios": "/Port-de-MDOS-iOS",
                "windows": "/Port-de-MDOS-Windows",
                "linux": "/Port-de-MDOS-Linux"
            },
            "branch_structure": {
                "main": "main",
                "development": "dev",
                "ports": "ports/*"
            }
        }
        
    def create_port_template(self, os_type):
        return {
            "os": os_type,
            "base_structure": self.get_base_structure(),
            "specific_configs": self.get_os_specific(os_type)
        }
        
    def get_base_structure(self):
        return {
            "core": ["system_core", "memory_manager", "process_handler"],
            "modules": ["avatar_system", "security", "updater"],
            "configs": ["os_specific", "hardware_config", "permissions"]
        }
        
    def get_os_specific(self, os_type):
        configs = {
            "android": {
                "manifest": "AndroidManifest.xml",
                "permissions": "android.permissions",
                "activity": "MainActivity"
            },
            "ios": {
                "info": "Info.plist",
                "permissions": "ios.permissions",
                "viewcontroller": "MainViewController"
            }
        }
        return configs.get(os_type, {})