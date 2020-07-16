""" Settings that you can use to override the default_settings.py """
from golinks import default_settings

locals().update(default_settings.__dict__)

'''
# Unix/Mac - 4 initial slashes in total
'sqlite:////absolute/path/to/foo.db'

# Windows
'sqlite:///C:\\path\\to\\foo.db'

# Windows alternative using raw string
r'sqlite:///C:\path\to\foo.db'
'''
SQLALCHEMY_DATABASE_URI = 'sqlite:///D:\\Git\\go-links-master\\db\\db.sqlite'
SECRET_KEY = 'CHANGE_ME'
