import unittest
from DIY_11_3_employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.man = Employee("Jan", "Peck", 2000)
        self.man.give_reise(150)

    def test_slow_me_person(self):

        self.assertNotEqual("Jan Peck 2150", self.man.slow_me_person)


if __name__ == '__main__':
    unittest.main()
