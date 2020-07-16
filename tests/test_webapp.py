from golinks.webapp import WEBAPP
from golinks.models import DB
import unittest
import flask


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        WEBAPP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        WEBAPP.config['TESTING'] = True
        self.webapp = WEBAPP
        self.app = WEBAPP.test_client()
        with WEBAPP.app_context():
            DB.init_app(WEBAPP)
            DB.create_all()

    def test_index_200(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'

    def test_go_link_redirect(self):
        with self.webapp.test_request_context('/'):
            assert flask.request.path == '/'


if __name__ == '__main__':
    unittest.main()
