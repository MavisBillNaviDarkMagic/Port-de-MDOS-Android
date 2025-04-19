class UserProtectionSystem:
    def __init__(self):
        self.protection_matrix = {
            "harmful_content": {
                "adult": "irreversible_block",
                "violence": "irreversible_block",
                "harmful_behavior": "irreversible_block",
                "animal_abuse": "irreversible_block"
            },
            "general_actions": {
                "safe_content": "revertible",
                "normal_actions": "revertible",
                "system_changes": "revertible"
            }
        }
        
    def check_action_type(self, action):
        """Verifica si una acción es reversible"""
        if any(key in str(action).lower() for key in self.protection_matrix["harmful_content"]):
            return {
                "reversible": False,
                "protection": "permanent",
                "reason": "harmful_content_protection"
            }
        return {
            "reversible": True,
            "protection": "standard",
            "type": "normal_action"
        }
        
    def process_user_request(self, user_id, action_type, content):
        """Procesa una solicitud de usuario"""
        action_check = self.check_action_type(content)
        if not action_check["reversible"]:
            return {
                "status": "protected",
                "message": "Esta acción no puede ser revertida por tu seguridad",
                "allowed": False
            }
        return {
            "status": "allowed",
            "reversion_allowed": True,
            "action_type": "safe"
        }
        
    def register_protected_action(self, user_id, action_data):
        """Registra una acción protegida"""
        return {
            "user": user_id,
            "action": "permanently_logged",
            "protection": "active",
            "revertible": False
        }