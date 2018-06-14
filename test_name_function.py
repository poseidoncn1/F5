import unittest
from unittest import TestSuite
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        # """能够正确处理像Janis Joplin这样的名字吗？"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
        self.assertEqual(1,1)
        self.assertEqual(1,2)
        self.assertNotEqual(True,False)
        self.assertTrue(1)
        self.assertFalse(None)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)



#loader使用unittest.TestLoader().loadTestsFromTestCase(class_instances)
#unittest.TestLoader().loadTestsFromTestName(moudle.classname)
#runner.run()
# suite = unittest.TestLoader().loadTestsFromTestCase(NamesTestCase)
#
# unittest.TextTestRunner(verbosity = 2).run(suite)

#自己自动执行调用
if __name__ == '__main__':
    unittest.main()

#使用suite.addTest(class_instances)单个suite
# if __name__ =='__main__':#这个可以决定执行顺序
#     suite = unittest.TestSuite()
#     test = [NamesTestCase("test_split")]
#     suite.addTests(test)
#     unittest.TextTestRunner(verbosity = 2).run(suite)



#使用unittest.TestSuite(iterable)
# if __name__ == '__main__':
#     site = ['test_split','test_first_last_name']
#     suite = unittest.TestSuite(map(NamesTestCase,site))
#     unittest.TextTestRunner(verbosity = 2).run(suite)
