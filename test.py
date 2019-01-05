import unittest
from app import app, db

# Set up test database
TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + TEST_DB
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    # Executed after each test
    def tearDown(self):
        pass

    # Helper methods
    def register(self, username, email, password, confirm_password):
        return self.app.post(
            '/signup',
            data=dict(username=username, email=email, password=password, confirm_password=confirm_password),
            follow_redirects=True
        )

    def login(self, username, password):
        return self.app.post(
            '/login',
            data=dict(username=username, password=password),
            follow_redirects=True
        )

    def reset_password(self, email):
        return self.app.post(
            '/reset_password',
            data=dict(email=email),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True
        )

    # Tests
    # test main page returns 200 response
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Ensure that homepage loads correctly
    def test_index_loads(self):
        response = self.app.get('/', content_type='html/text')
        self.assertTrue(b'Where are you going?' in response.data)

    # Ensure that login loads correctly
    def test_login_loads(self):
        response = self.app.get('/login', content_type='html/text')
        self.assertTrue(b'Log In' in response.data)

    # Ensure that login behaves with correct credentials
    def test_correct_login(self):
        self.register('Paulpaul', 'p@p.com', 'Paulpassword', 'Paulpassword')
        response = self.login('Paulpaul', 'Paulpassword')
        self.assertIn(b'Paul', response.data)

    # Ensure that reset password works
    def test_reset_password(self):
        self.register('Paulpaul', 'p@p.com', 'Paulpassword', 'Paulpassword')
        response = self.reset_password('p@p.com')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'An email', response.data)

    # Ensure that signup loads correctly
    def test_signup_loads(self):
        response = self.app.get('/signup', content_type='html/text')
        self.assertTrue(b'Leap Card (optional)' in response.data)

    # Ensure that registration page behaves correctly
    def test_valid_user_registration(self):
        response = self.register('Paulpaul', 'p@p.com', 'Paulpassword', 'Paulpassword')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Forgot Password', response.data)

    # Ensure that password confirmation works
    def test_invalid_user_registration_different_passwords(self):
        response = self.register('Paulpaul', 'p@p.com', 'Paulpassword', 'Paulpasswordssssss')
        self.assertIn(b'Field must be equal to password.', response.data)

    # Ensure that history appears after logging in
    def test_history_appears_for_login(self):
        self.register('Paulpaul', 'p@p.com', 'Paulpassword', 'Paulpassword')
        response = self.login('Paulpaul', 'Paulpassword')
        self.assertIn(b'History', response.data)

    # Ensure that reset password page loads correctly
    def test_reset_loads(self):
        response = self.app.get('/reset_password', content_type='html/text')
        self.assertTrue(b'Reset Password' in response.data)

    # Ensure that map page requires addresses input
    def test_map_requires_addresses(self):
        response = self.app.get('/map', follow_redirects=True)
        self.assertTrue(b'Dublin Bikes' not in response.data)

    # Ensure that logout behaves correctly
    def test_history_button(self):
        self.register('Paulpaul', 'p@p.com', 'Paulpassword', 'Paulpassword')
        self.login('Paulpaul', 'Paulpassword')
        self.logout()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b"Let's Go", response.data)


if __name__ == "__main__":
    unittest.main()
