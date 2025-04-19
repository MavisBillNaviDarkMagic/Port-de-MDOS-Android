class UserController:
    def __init__(self):
        self.user_settings = {
            "can_revert": True,
            "protected_categories": {
                "adult": "permanent_block",
                "violence": "permanent_block",
                "harmful": "permanent_block",
                "abuse": "permanent_block"
            },
            "regular_actions": {
                "app_settings": "revertible",
                "preferences": "revertible",
                "normal_content": "revertible"
            }
        }
        
    def check_reversion_permission(self, action_type, content):
        if any(category in str(content).lower() for category in self.user_settings["protected_categories"]):
            return {
                "allowed": False,
                "reason": "permanent_protection",
                "message": "Esta acción no puede ser revertida por tu seguridad"
            }
        return {
            "allowed": True,
            "type": "regular_action",
            "revertible": True
        }
        
    def process_user_request(self, user_id, request_type, content):
        permission = self.check_reversion_permission(request_type, content)
        if not permission["allowed"]:
            return {
                "status": "blocked",
                "protection": "active",
                "can_revert": False
            }
        return {
            "status": "processed",
            "reversion": "available",
            "protection": "standard"
        }
        
    def handle_reversion_request(self, user_id, action_id):
        return {
            "processed": True,
            "status": "reverted",
            "protection": "maintained"
        }