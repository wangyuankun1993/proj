from user import User
from admin import Admin
from privileges import Privileges

admin = Admin('Alice', 'Bob')
admin.show_privileges()