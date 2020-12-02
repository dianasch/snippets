import unittest
from werkzeug.security import (generate_password_hash, check_password_hash)

from server import app, current_user
from model import connect_to_db, db, test_data


class FlaskTests(unittest.TestCase):
    """Test routes for snippet app."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        test_data()

    def test_homepage_response(self):
        """Test response from homepage."""

        response = self.client.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        """Test that homepage loads correctly."""

        response = self.client.get('/')
        self.assertIn(b'make an original Taylor Swift song snippet', response.data)

    def test_registration(self):
        """Test create an account route."""

        response = self.client.post("/users",
                                data=dict(email="test@test.com", password="password"),
                                follow_redirects=True)
        self.assertIn(b"Account created!", response.data)

    def test_registration_with_existing_email(self):
        """Test creating an account with an existing email."""

        response = self.client.post("/users",
                                data=dict(email="user@user.com", password="password"),
                                follow_redirects=True)
        self.assertIn(b"There is already an account associated with this email.", response.data)

    def test_login(self):
        """Test login route."""

        response = self.client.post("/login",
                                data=dict(email="user@user.com", password="password"),
                                follow_redirects=True)
        self.assertIn(b"Logged in!", response.data)

    def test_login_bad_password(self):
        """Test log in with a bad password."""

        response = self.client.post("/login",
                        data=dict(email="user@user.com", password="wrong_password"),
                        follow_redirects=True)
        self.assertIn(b"Email and password do not match.", response.data)

    def test_login_bad_email(self):
        """Test log in with a bad email."""

        response = self.client.post("/login",
                data=dict(email="bad_email@user.com", password="password"),
                follow_redirects=True)
        self.assertIn(b"There is no account associated with this email.", response.data)

    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()



# class FlaskTestsLoggedIn(unittest.TestCase):
#     """Test routes for users that are logged in."""

#     def setUp(self):
#         self.client = app.test_client()
#         app.config['TESTING'] = True
#         app.config['SECRET_KEY'] = 'key'
#         self.client = app.test_client()

#         with self.client as c:
#             with c.session_transaction() as sess:
#                 sess['user_id'] = 1

#     def test_albums(self):
#         """Test that albums page loads correctly."""

#         response = self.client.get('/albums')
#         self.assertIn(b'Select an album to view more details', response.data)

    # def test_albums(self):
    #     """Test that albums page loads correctly."""

    #     response = self.client.get('/albums')
    #     self.assertIn(b'Select an album to view more details', response.data)

    # def test_correct_login(self):
    #     """Test login success with correct credentials."""

    #     response = self.client.post(
    #         '/login',
    #         data=dict(email="test@test.com", password="test",
    #         follows_redirect=True)
    #     )
    #     self.assertIn(b'Logged in!', response.data)
    

if __name__ == '__main__':
    unittest.main()