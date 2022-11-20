import unittest
from admin_9_7 import User

class TestAdmin(unittest.TestCase):


    def setUp(self):

        self.user_1 = User('mister', 'ikx', 'kein', '100')
        self.user_1.great_user()

    def test_great_user(self):
        self.user_1.great_user()
        self.assertEqual("I congratulate you, Andrii Yarovski! ", self.user_1.great_user())


if __name__ == '__main__':
    unittest.main()
