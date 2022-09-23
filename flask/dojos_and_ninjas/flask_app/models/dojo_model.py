from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja_model

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for one_dojo in result:
            dojos.append(cls(one_dojo))
        return dojos

    @classmethod
    def view_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def view_one_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        if len(result) > 0:
            dojo_instance = cls(result[0])
            ninja_list = []
            for row_from_db in result:
                ninja_data = {
                    'id': row_from_db['ninjas.id'],
                    'first_name': row_from_db['first_name'],
                    'last_name': row_from_db['last_name'],
                    'age': row_from_db['age'],
                    'created_at': row_from_db['ninjas.created_at'],
                    'updated_at': row_from_db['ninjas.updated_at'],
                    'dojo_id': row_from_db['dojo_id']
                }
                ninja_instance = ninja_model.Ninja(ninja_data)
                ninja_list.append(ninja_instance)
            dojo_instance.ninja_list = ninja_list
            return dojo_instance
        return False 