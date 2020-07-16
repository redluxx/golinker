""" Avoid making changes in this file, use the settings.py file """


SQLALCHEMY_DATABASE_URI = 'sqlite:///D:\\Git\\go-links-master\\db\\db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEMO_RECORDS = [
    ('mail', 'https://mail.google.com'),
    ('git', 'https://gitlab.com{/search?terms=^}'),
    ('github', 'https://github.com{/search?terms=^}'),
    ('in', 'https://www.linkedin.com'),
    ('fb', 'https://www.facebook.com')
]

ADD_DEMO_RECORDS = True

TITLE = 'Go Links'
SUB_TITLE = 'Short link service for internal use'

PORT = 5000
HOSTNAME = 'localhost'

DEBUG = False
SECRET_KEY = 'CHANGE_ME'

# Our HTML Form Buttons
CREATE_UPDATE_TEXT = 'Save'
SEARCH_TEXT = 'Search'
DELETE_TEXT = 'Delete'
