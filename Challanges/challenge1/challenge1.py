import unittest
from selenium import webdriver


class Challenge1(unittest.TestCase):
    """This challenge is to make sure that google search is launched properly"""

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("../drivers/chromedriver")

    def tearDown(self) -> None:
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)


if __name__ == '__main__':
    unittest.main()
