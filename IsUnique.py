import unittest

def unique(string):
    isUnique = []

    for c in string:
        if not c in isUnique:
            isUnique.append(c)
        else:
            return False
    return True


class Test(unittest.TestCase):
    dataT = [('abcd'),('teach'),('')]
    dataF = [('23ds2'),('hb627jh=j ()')]

    def test_unique(self):
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)

        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()
