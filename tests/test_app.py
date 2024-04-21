import unittest
import app

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
