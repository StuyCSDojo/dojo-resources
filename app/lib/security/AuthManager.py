import passlib.hash
import pymongo

import security_utils

client = pymongo.MongoClient()

class AuthManager(object):

    def __init__(self, db):
        self.db = client[db]

    def is_registered(self, username):
        user_entry = self.db.users.find_one({
            'username': username
        })
        return bool(user_entry)

    def is_admin(self, username):
        user_entry = self.db.admins.find_one({
            'username': username
        })
        return bool(user_entry)

    def is_developer(self, username):
        user_entry = self.db.developers.find_one({
            'username': username
        })
        return bool(user_entry)

    def register(self, username, password, confirmation_password):
        if password != confirmation_password:
            return False, 'Passwords do not match.'
        elif self.is_registered(username):
            return False, 'User already exists.'
        else:
            self.db.users.insert_one({
                'username': username,
                'passhash': security_utils.secure_hash_password(password)
            })
            return True, 'Successfully registered!'

    def login(self, username, password):
        user_entry = self.db.users.find_one({
            'username': username
        })

        if not user_entry:
            return False, 'User does not exist.'

        hashed_password = user_entry.get('passhash')
        if passlib.hash.argon2.verify(password, hashed_password):
            return True, 'Sucessfully logged in!'
        else:
            return False, 'Invalid username or password.'

    def drop_user(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist.'
        else:
            self.db.users.remove({
                'username': username
            })
            self.drop_admin(username)
            self.drop_developer(username)
            return True, 'User dropped!'

    def drop_admin(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist.'
        elif not self.is_admin(username):
            return False, 'User is not an admin.'
        else:
            self.db.admins.remove({
                'username': username
            })
            self.drop_developer(username)
            return True, 'Admin dropped!'

    def drop_developer(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist.'
        elif not self.is_developer(username):
            return False, 'User is not a developer.'
        else:
            self.db.developers.remove({
                'username': username
            })
            return True, 'Developer dropped!'

    def make_admin(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist.'
        elif self.is_admin(username):
            return False, 'User is already an admin.'
        else:
            self.db.admins.insert_one({
                'username': username
            })
            return True, 'User is now an admin!'

    def make_developer(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist.'
        elif self.is_developer(username):
            return False, 'User is already a developer.'
        else:
            self.db.developers.insert_one({
                'username': username
            })
            self.make_admin(username)
            return True, 'User is now a developer!'
