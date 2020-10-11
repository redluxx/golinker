""" GoRecord Model that is stored via SQLAlchemny
"""
import re
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class GoRecord(DB.Model):
    """ GoRecord Object """
    __tablename__ = 'gorecord'
    gid = DB.Column(DB.Integer ,primary_key=True)
    name = DB.Column(DB.String(50), unique=True)
    url = DB.Column(DB.String(255))
    favicon = DB.Column(DB.String(255))
    owner = DB.Column(DB.String(50))
    visits = DB.Column(DB.Integer,default=0)

    def __init__(self, name, url, favicon=None, owner=None):
        """ Make a new GoRecord """
        self.name = name
        self.url = url
        self.favicon = favicon
        self.owner = owner
        

    def __repr__(self):
        """ Pretty """
        return "<GoRecord {.name}>".format(self)

    
    @property
    def url_plain(self):
        return re.sub('{.*}', '', self.url)

    def link(self, optional=None):
        """ The real link based on the optional stuff """
        url_optional = ''

        try:
            url_optional = re.match('.*{(.*)}.*', self.url)
            url_optional = url_optional.groups()[0]
        except AttributeError:
            url_optional = ''

        if optional:
            optional_args = url_optional.replace('^', optional)
            return '{}{}'.format(self.url_plain, optional_args)

        return self.url_plain

class user(DB.Model):
    """ User Object - Currently not used"""
    __tablename__ = 'users'
    gid = DB.Column(DB.Integer ,primary_key=True)
    user = DB.Column(DB.String(50), unique=True)
    pwd = DB.Column(DB.String(255))
    
    def __init__(self, user, pwd):
        """ Make a new GoRecord """
        self.user = user
        self.pwd = pwd

class Settings(DB.Model):
    """ Settings storage """
    __tablename__ = 'settings'
    name = DB.Column(DB.String(50), primary_key=True, unique=True)
    status = DB.Column(DB.Boolean, default=False)
    comment = DB.Column(DB.String(255))

    def __init__(self, name, status, comment):
        """ New setting """
        self.name = name
        self.status = status
        self.comment = comment

    def setup():
        vals = {"ADMIN" : "Currently not used.", "EDITOR" : "Editing of configured links", "DARKMODE" : "Currently not used."}
        for name, comment in vals.items():
            setting = Settings.query.filter_by(name=name).first()
            if not setting:
                settings = Settings(name, False, comment)
                DB.session.add(settings)
                DB.session.commit()