import unittest as ut

class Test_TestPython(ut.TestCase):
    def test_python(self):
        self.assertEqual(4, 4)

    def test_another(self):
        self.assertEqual(100, 100)

    def test_krishna(self):
        self.assertEqual(200, 67)

if __name__ == '__main__':
    ut.main()
