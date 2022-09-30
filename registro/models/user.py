from  registro.config.mysqlconnection import *

class User:
    db_name="login_registration"

    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['first_name']
        self.apellido = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        # no se encontró un usuario coincidente
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email, password) VALUES (%(nombre)s,%(apellido)s,%(email)s, %(password)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)