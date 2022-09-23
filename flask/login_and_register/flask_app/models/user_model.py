from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM  users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def get_one_by_email(cls,data):
        query = "SELECT * FROM  users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_users = []
            for one_user in results:
                all_users.append(cls(one_user))
            return all_users
        return False

    @classmethod
    def update_one(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete_one(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate_registration(data):
        is_valid = True
        
        if len(data['first_name']) <= 0:
            flash('First Name is required')
            is_valid = False
        
        if len(data['last_name']) <= 0:
            flash('Last Name is required')
            is_valid = False
        
        if len(data['email']) <= 0:
            flash('Email is required')
            is_valid = False
        
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False

        if len(data['password']) <= 0:
            flash('Password is required')
            is_valid = False

        if len(data['confirm_password']) <= 0:
            flash('Confirm Password is required')
            is_valid = False
        
        elif data['password'] != data['confirm_password']:
            flash('PASSWORDS DO NOT MATCH!')
            is_valid = False
        
        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        
        if len(data['email']) <= 0:
            flash('Email is required')
            is_valid = False
        
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False

        if len(data['password']) <= 0:
            flash('Password is required')
            is_valid = False
        
        if is_valid: 
            #check the password hash
            incoming_user = User.get_one_by_email({ 'email' : data['email']})
            if not bcrypt.check_password_hash(incoming_user.password, data['password']):
                flash('Incorrect Password')
                is_valid = False
            else:
                session['user_id'] = incoming_user.id

        return is_valid    