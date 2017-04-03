import unittest

from free_tools import get_readme


class Test_Get_Readme(unittest.TestCase):
    def test_get_readme(self):
        expect_contains = "free tools for great good"
        observed = get_readme.get_readme()
        self.assertIn(expect_contains, observed.lower())

    def test_get_readme_all_caps(self):
        expect_contains = "FREE TOOLS FOR GREAT GOOD"
        observed = get_readme.get_readme_all_caps()
        self.assertIn(expect_contains, observed)

if __name__ == '__main__':
    unittest.main()
