from  registro.config.mysqlconnection import *

class Libro:
    db_name="login_registration"
    def __init__( self , data ):
        self.id=data['id']
        self.titulo = data['titulo']
        self.owner= data['owner']
        self.owner_id= data['owner_id']

    @classmethod
    def create(cls,data):
        query = "INSERT INTO books (titulo, owner) VALUES (%(titulo)s,%(owner)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all_books(cls):
        query = "SELECT books.id,books.titulo, CONCAT(users.first_name,' ',users.last_name) as owner,users.id as owner_id  FROM books INNER JOIN users ON (books.owner=users.id);"
        result = connectToMySQL(cls.db_name).query_db(query)
        libros=[]
        for r in result:
            libros.append(cls(r))

        return libros

    @classmethod
    def get_books_by_owner(cls,data):
        query = "SELECT books.id,books.titulo, CONCAT(users.first_name,' ',users.last_name) as owner,users.id as owner_id  FROM books INNER JOIN users ON (books.owner=users.id) where books.owner= %(owner_id)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        libros=[]
        for r in result:
            libros.append(cls(r))
        return libros


    @classmethod
    def get_libro_by_id(cls,data):
        query = "SELECT books.id,books.titulo, CONCAT(users.first_name,' ',users.last_name) as owner,users.id as owner_id  FROM books INNER JOIN users ON (books.owner=users.id) where books.id= %(libro_id)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])

    @classmethod
    def save(cls,data):
        query = "UPDATE books SET titulo= %(titulo)s where books.id= %(libro_id)s ;"
        return connectToMySQL(cls.db_name).query_db(query, data)
        