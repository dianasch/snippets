import unittest
from server import app
from model import connect_to_db

class FlaskTests(unittest.TestCase):
    """Test routes for snippet app."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage_response(self):
        """Test response from homepage."""

        response = self.client.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        """Test that homepage loads correctly."""

        response = self.client.get('/')
        self.assertIn(b'make an original Taylor Swift song snippet', response.data)

    def test_correct_login(self):
        """Test login success with correct credentials."""
    
    def incorrect_login(self): 

    


if __name__ == '__main__':
    unittest.main()