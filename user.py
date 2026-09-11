from abc import ABC, abstractmethod
class User(ABC):
    _name: str
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value

            
    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def has_permission(self, permission):
        pass
    

        
