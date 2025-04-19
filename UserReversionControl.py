class UserReversionControl:
    def __init__(self):
        self.permanent_blocks = {
            "adult_content": True,
            "violence": True,
            "harmful_behavior": True,
            "animal_cruelty": True,
            "explicit_content": True
        }
        
        self.reversion_settings = {
            "general_reversion": True,
            "harmless_content": True,
            "safe_actions": True
        }
    
    def evaluate_reversion_request(self, action_type, content_data):
        harmful_content = self.check_harmful_content(content_data)
        if harmful_content:
            return {
                "allowed": False,
                "reason": "permanent_restriction",
                "message": "Esta acción no puede ser revertida por motivos de protección"
            }
        return {
            "allowed": True,
            "type": "safe_reversion",
            "status": "processing"
        }
    
    def check_harmful_content(self, content):
        harmful_patterns = [
            "adult", "violence", "explicit",
            "abuse", "cruelty", "harmful",
            "dangerous", "inappropriate"
        ]
        return any(pattern in str(content).lower() for pattern in harmful_patterns)
    
    def register_user_action(self, user_id, action):
        return {
            "user": user_id,
            "action": action,
            "revertible": not self.check_harmful_content(action),
            "timestamp": "current_time"
        }