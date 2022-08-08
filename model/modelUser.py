from model.entidades.user import User

class ModelUser():
	@classmethod #permite usar la función sin instanciar la clase modelUser
	def login(self, db, user):
		try:
			cursor = db.connection.cursor()
			sql = "SELECT id, username, password, fullname FROM user WHERE username = '{}' ".format(user.username)
			cursor.execute(sql)
			row = cursor.fetchone()
			if row != None:
				user = User(row[0], row[1], user.check_password(row[2],user.password),row[3])
				return user
			else:
				return None
		except Exception as ex:
			raise Exception(ex)

	@classmethod
	def get_by_id(self, db, id):
		try:
			cursor = db.connection.cursor()
			sql = "SELECT id, username, fullname FROM user WHERE id = {}".format(id)
			cursor.execute(sql)
			row = cursor.fetchone()
			if row != None:
				logged_user = User(row[0], row[1], None, row[2])
				print(logged_user)
				return logged_user
			else:
				return None
		except Exception as ex:
			raise Exception(ex)