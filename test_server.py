import unittest
from server import app

class FlaskTests(unittest.TestCase):
    """Test routes for snippet app."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test homepage route."""

        result = self.client.get('/')
        self.assertIn(b'make an original Taylor Swift song snippet', result.data)


if __name__ == '__main__':
    unittest.main()