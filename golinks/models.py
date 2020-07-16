""" GoRecord Model that is stored via SQLAlchemny
"""
import re
from flask_sqlalchemy import SQLAlchemy
import golinks.utils as utils

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

    def url_checker(url):
        """ This is using a massive regex list 
            Remove the import and utilise the list ourselves """
        plain_url = re.sub('{.*}', '', url)
        return utils.valid_URL(plain_url)

    def faviconer(url):
        """ Set the favicon URL based on the domain supplied """
        plain_url = re.sub('{.*}', '', url)
        domain = plain_url.split('/')[2]
        favicon_path = "https://{0}/favicon.ico".format(domain)
        return favicon_path

        

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
