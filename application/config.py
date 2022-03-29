import os


class Config(object):
    SECRET_KEY = b'\x1f2\x00L\xe4Fh\x1b\x89\x16\x9e\x85\xe3\xbac\xee{\x9e\r2\xef\x1d\xc5\xd2'
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///phone.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = '/uploads'


