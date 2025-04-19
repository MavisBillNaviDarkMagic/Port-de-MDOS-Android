class ReversionControl:
    def __init__(self):
        self.permanent_blocks = {
            "adult_content": True,
            "violence": True,
            "harmful_content": True,
            "animal_abuse": True
        }
        self.reversion_settings = {
            "allow_general_reversion": True,
            "block_harmful_reversion": True,
            "protection_level": "maximum"
        }
        
    def can_revert(self, action_type, content_data):
        if action_type in self.permanent_blocks:
            return {
                "revertible": False,
                "reason": "permanent_block",
                "protection": "active"
            }
        return {
            "revertible": True,
            "protection": "standard"
        }
        
    def protect_action(self, action_type):
        return {
            "protection": "permanent",
            "reversible": False,
            "type": action_type
        }
        
    def analyze_content(self, content):
        return {
            "harmful": self.check_harmful_content(content),
            "block_reversion": True if self.check_harmful_content(content) else False
        }
        
    def check_harmful_content(self, content):
        harmful_indicators = [
            "adult_content", "violence", "abuse",
            "harmful", "dangerous", "explicit"
        ]
        return any(indicator in str(content).lower() for indicator in harmful_indicators)