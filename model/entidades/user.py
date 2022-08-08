from werkzeug.security import check_password_hash
#from werkzeug.security import generate_password_hash # para generar el pass hashed 
from flask_login import UserMixin


class User(UserMixin):
	def __init__(self, id, username, password, fullname= "") -> None:
		self.id = id
		self.username = username
		self.password = password
		self.fullname = fullname

	@classmethod
	def check_password(self, hashed_password, password):
		return check_password_hash(hashed_password, password)

# para generar el password hashed y verlo por consola print(generate_password_hash("123456"))