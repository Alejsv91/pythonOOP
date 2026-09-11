from adminUser import AdminUser
from regularUser import RegularUser

user1= AdminUser("Alvaro")
user2= RegularUser("Pedro")

print(user1.has_permission('delete'))
print(user2.has_permission('delete'))