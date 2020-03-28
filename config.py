import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'k#0!fcYMPBtgHHDXrol8v+Sf5RG!t1Zi'
