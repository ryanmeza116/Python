from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = "belt_test_1"
class Sighting:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.location = db_data['location']
        self.what_happened = db_data['what_happened']
        self.date = db_data['date']
        self.number = db_data['number']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.users_id = db_data['users_id']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO sighting (location, what_happened, date, number, users_id) VALUES (%(location)s,%(what_happened)s,%(date)s,%(number)s,%(users_id)s);"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sighting"
        results = connectToMySQL(db).query_db(query)
        print('RESULTS OF GET ALL ARE:', results)
        all_sightings = []
        for row in results:
            all_sightings.append(cls(row))
        return all_sightings

    @classmethod
    def join_all(cls):
        query = "SELECT * FROM sighting JOIN users on users.id = sighting.users_id;"
        results = connectToMySQL(db).query_db(query)
        print('RESULTS OF JOIN ALL ARE: ', results)
        all_joined_sightings = []
        for row in results:
            all_joined_sightings.append(row)
        print('ALL JOINED SIGHTINGS CLASS OBJECT RESULT: ', all_joined_sightings)
        print('FIRST JOINED SIGHTINGS CLASS OBJECT RESULT: ')
        return all_joined_sightings

    @classmethod
    def get_one(cls,data):
        query = "SELECT * from sighting WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM sighting WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update(cls,data):
        print('*****************')
        print('RUNNING UPDATE QUERY')
        print('****************')
        query = "UPDATE sighting SET location=%(location)s, what_happened=%(what_happened)s, date=%(date)s, number=%(number)s,updated_at=NOW() WHERE id = %(id)s;"
        results =  connectToMySQL(db).query_db(query,data)
        print('')
        print('')
        print('')
        print('')
        print ("RESULTS OF UPDATE ARE:", results)
        return results


    @staticmethod
    def validate_sighting(sighting):
        print('******************')
        print("STARTING VALIDATIONS")
        print('***************')
        is_valid = True
        if len(sighting['location']) < 2:
            is_valid = False
            flash("Location Must be at least 2 characters", "sighting")
        if len(sighting['what_happened']) < 2:
            is_valid = False
            flash("Event must be at least 3 characters","sighting")
        if sighting['date'] == "":
            is_valid = False
            flash('Please enter a date', 'sighting')
        if sighting['number'] == 0:
            is_valid = False
            flash("Must be at least one Squatch present to process report","sighting")
        print('************')
        print("VALIDATION COMPLETE, RESULT IS", is_valid)
        return is_valid
