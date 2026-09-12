from .user import User

class AdminUser(User):
    
    def __init__(self, name: str):
        super().__init__(name)
        self.permissions = {
            "read": True,
            "write": True,
            "delete": True,
            "update": True
        }
        
        self.name = name
        self.role = 'Admin'
        
    def get_role(self):
        return self.role        
        
    def has_permission(self, permission: str):
        return self.permissions[permission]