from src import app
import unittest
import json


class BaseTestCases(unittest.TestCase):
    def test_not_found_path(self):
        tester = app.test_client(self)
        response = tester.get('a', content_type='html/text')
        self.assertEqual(response.status_code, 404)
        self.assertTrue(b'Not Found' in response.data)


if __name__ == '__main__':
    unittest.main()
