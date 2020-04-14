import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'k#0!fcYMPBtgHHDXrol8v+Sf5RG!t1Zi'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('FLASK_MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('FLASK_MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('FLASK_MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('FLASK_MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASSWORD')
    ADMINS = ['justin@somuchuptime.com']
    POSTS_PER_PAGE = 25
