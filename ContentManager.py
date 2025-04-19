class ContentManager:
    def __init__(self):
        self.user_reversion = UserReversionControl()
        self.content_status = {
            "safe_content": True,
            "protection_active": True,
            "user_safety": "maximum"
        }
        
    def process_user_action(self, user_id, action_type, content):
        evaluation = self.user_reversion.evaluate_reversion_request(action_type, content)
        if not evaluation["allowed"]:
            self.log_permanent_action(user_id, content)
            
        return {
            "processed": True,
            "revertible": evaluation["allowed"],
            "protection": "active"
        }
        
    def log_permanent_action(self, user_id, content):
        return {
            "user": user_id,
            "content": "permanently_logged",
            "reversion": "blocked",
            "protection_reason": "user_safety"
        }
        
    def allow_safe_reversion(self, user_id, action_id):
        return {
            "allowed": True,
            "type": "safe_content",
            "user_protected": True
        }