from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

db = "belt_test_2"
class Tree:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.species = db_data['species']
        self.location = db_data['location']
        self.reason = db_data['reason']
        self.date_planted = db_data['date_planted']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.users_id = db_data['users_id']
        self.user = None

    @classmethod
    def save(cls,data):
        query = "INSERT INTO trees (species, location, reason, date_planted, created_at, updated_at, users_id) VALUES (%(species)s, %(location)s, %(reason)s, %(date_planted)s, NOW(), NOW(), %(users_id)s);" 
        return connectToMySQL(db).query_db(query, data)


    @classmethod
    def join_all(cls):
        query = "SELECT * FROM trees JOIN user ON users_id = user.id;"
        results = connectToMySQL(db).query_db(query)
        print('RESULTS OF JOIN ALL ARE: ', results)
        all_joined_trees = []
        for row in results:
            tree = cls(row)

            user_data= {
                "id" : row['user.id'],
                "first_name": row['first_name'],
                "last_name" : row['last_name'],
                "email" : row['email'],
                "password" : row['password'],
                "created_at" : row['user.created_at'],
                "updated_at" : row['user.updated_at'],
            }
            user = User(user_data)
            tree.user = user
            all_joined_trees.append(tree)
        print('ALL JOINED SIGHTINGS CLASS OBJECT RESULT: ', all_joined_trees)
        return all_joined_trees

    @classmethod
    def get_one(cls,data):
        query = "SELECT * from trees WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_user_and_tree(cls,data):
        query = "SELECT * FROM trees JOIN user on users_id = user.id WHERE trees.id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        print('*************')
        print("RESULTS ARE", results)
        row = results[0]
        
        # joined_user_and_tree = []
        # for row in results:
        tree = cls(row)
        user_data= {
            "id" : row['user.id'],
            "first_name": row['first_name'],
            "last_name" : row['last_name'],
            "email" : row['email'],
            "password" : row['password'],
            "created_at" : row['user.created_at'],
            "updated_at" : row['user.updated_at'],
        }
        user = User(user_data)
        tree.user = user
        #     joined_user_and_tree.append(tree)
        #     print("******RESULTS ARE", results)
        #     print('******USER DATA IS: ', user_data)
        return tree

    # @classmethod
    # def user_and_tree(cls,id):
    #     query = "SELECT * FROM trees JOIN user on users_id = user.id WHERE trees.id = %(id)s;"
    #     results = connectToMySQL(db).query_db(query,id)
    #     user_and_tree = []
    #     for row in results:
    #         user_and_tree.append(row)
    #     return user_and_tree

    @classmethod
    def update(cls,data):
        print('*****************')
        print('RUNNING UPDATE QUERY')
        print('****************')
        query = "UPDATE trees SET species=%(species)s, location=%(location)s, reason=%(reason)s, date_planted=%(date_planted)s,updated_at=NOW() WHERE id = %(id)s;"
        results =  connectToMySQL(db).query_db(query,data)
        print ("RESULTS OF UPDATE ARE:", results)
        return results

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM trees WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)

    @staticmethod
    def validate_tree(tree):
        print('******************')
        print("STARTING VALIDATIONS")
        print('***************')
        is_valid = True
        if len(tree['species']) < 5:
            is_valid = False
            flash("Location Must be at least 5 characters", "tree")
        if len(tree['location']) < 2:
            is_valid = False
            flash("Event must be at least 2 characters","tree")
        if len(tree['reason']) <= 0:
            is_valid = False
            flash('Please enter a reason for planting', "tree")
        if tree['date_planted'] == '':
            is_valid = False
            flash("Please enter a valid date","tree")
        print('************')
        print("VALIDATION COMPLETE, RESULT IS", is_valid)
        return is_valid
