import unittest

from free_tools import get_readme


class Test_Get_Readme(unittest.TestCase):
    def test_get_readme(self):
        expect_contains = "free tools for great good"
        observed = get_readme.get_readme()
        self.assertIn(expect_contains, observed.lower())


if __name__ == '__main__':
    unittest.main()
