import unittest
from server import app
from model import connect_to_db

class FlaskTests(unittest.TestCase):
    """Test routes for snippet app."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test homepage route."""

        result = self.client.get('/')
        self.assertIn(b'make an original Taylor Swift song snippet', result.data)

    # def test_albums_page(self):
    #     """Test albums route."""

    #     result = self.client.get('/albums')
    #     self.assertIn(b'Taylor Swift album', result.data)


if __name__ == '__main__':
    unittest.main()