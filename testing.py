import os
import webstart
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, webstart.app.config['DATABASE'] = tempfile.mkstemp()
        webstart.app.config['TESTING'] = True
        self.app = webstart.app.test_client()
        webstart.init_db()

    def poop(self):
    	self.assertTrue(1 in [1,2])

    # def tearDown(self):
    #     os.close(self.db_fd)
    #     os.unlink(webstart.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()