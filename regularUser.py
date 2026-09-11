from user import User

class RegularUser(User):
    def __init__(self, name):
        self.permissions = {
            "read": True,
            "write": False,
            "delete": False,
            "update": False
        }
        self.name = name
        self.role = 'Regular'
        
    def get_role(self):
        return self.role 
        
        
    def has_permission(self, permission: str):
        return self.permissions[permission]
    