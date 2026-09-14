from datetime import date


class User:
    def __init__(self, date_of_birth: date, drive_license: bool):
        self.date_of_birth = date_of_birth
        self.drive_license = drive_license

    @property
    def age(self) -> int:
        today = date.today()

        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
    
def is_adult(func):
    def wrapper(user: User):
        if user.age < 18:
            raise ValueError(" User is not an adult")
        else:
            print("User is adult")
        return func(user)
    return wrapper
            
@is_adult
def user_can_drive(user: User):
    if user.drive_license:
        print("User can drive")
    else: 
        print("User can't drive")
    
        
birthdate = date(2016,1,9)
user = User(birthdate, True)
user_can_drive(user)