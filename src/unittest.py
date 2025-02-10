import unittest

class Math(object):
    def add(self, x, y):
        return x+y
    def sub(self, x, y):
        return x-y

class testCaseMath(unittest.TestCase):
    def setUp(self):           
        self.math = Math()   # Math()的对象作为testCase的一个属性。

    def test_add(self):
        self.assertEqual(self.math.add(2, 3), 5)
        print("add")
    
    def test_sub(self):
        self.assertEqual(self.math.sub(30, 20), 10)
        print("sub")

if __name__ == '__main__':
    unittest.main()


