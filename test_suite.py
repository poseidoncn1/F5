import unittest

class Test(unittest.TestCase):
    def test1(self):
        assert(True == True)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test('test1')) # <----------------
    unittest.TextTestRunner().run(suite)
