''' Settings '''

'''
# Unix/Mac - 4 initial slashes in total
'sqlite:////absolute/path/to/foo.db'

# Windows
'sqlite:///C:\\path\\to\\foo.db'

# Windows alternative using raw string
r'sqlite:///C:\path\to\foo.db'
'''
SQLALCHEMY_DATABASE_URI = 'sqlite:///D:\\Git\\go-links-master\\db\\db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'CHANGE_ME'
DEBUG = True

DEMO_RECORDS = [
    ('mail', 'https://mail.google.com', 'https://ssl.gstatic.com/ui/v1/icons/mail/images/favicon5.ico'),
    ('github', 'https://github.com{/search?terms=^}', ''),
    ('in', 'https://www.linkedin.com', ''),
    ('reddit', 'https://www.reddit.com', '')
]

ADD_DEMO_RECORDS = True

TITLE = 'Go Links'

PORT = 5000
HOSTNAME = 'localhost'