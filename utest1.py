import unittest
# assert 1 == 1
# assert '1' not in '24'
class TestStringMethods(unittest.TestCase):

    def test_is_string(self):
        self.assertEqual(type("aa"), str)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
    
    def test_error_raise(self):
        s = 'hello world'
        # with self.assertRaises(TypeError):
        s.split(2)


if __name__=='__main__':
    unittest.main()
