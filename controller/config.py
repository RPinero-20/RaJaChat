class Config:
	SECRET_KEY = 'my_secret_key'

class DevelopmentConfig(Config):
	Debug = True
	MYSQL_HOST = 'localhost'
	MYSQL_USER = 'root'
	# MYSQL_PASSWORD = 'my_secret_key'
	MYSQL_DB = 'rajachat_login'

config = {
	'development':DevelopmentConfig
}