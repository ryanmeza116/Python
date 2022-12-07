from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "users_schema"
    def __init__(self,data):
        # Why do we import data?
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        
        print("LINE 17 USER.PY")
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        all_users = []
        for i in results:
            all_users.append(cls(i))
            # why does cls get passed into the append
        print(all_users)
        return all_users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        result = connectToMySQL(cls.db).query_db(query,data)
        # Why does data get passed into the class method? 
        return result

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        print(f"GET ONE RESULT IS", result)
        return cls(result[0])
        # return result
        # Only started working after i referenced the cls and index of 0 -- why?
        # Result from mysqlconnection returns a list. Even with one object in the list, we need to reference it. 
# potentially need to store result in list and ref 0 index in return

    @classmethod
    def delete_one(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)