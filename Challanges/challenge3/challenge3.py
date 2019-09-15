import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):
    """This challenge requires to check if Porsche is listed under Exotic car search"""

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("../drivers/chromedriver")

    def tearDown(self) -> None:
        self.driver.close()

    def test_challenge3git (self):
        # launch the site
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart USA", self.driver.title)

        self.driver.maximize_window()

        # most popular table
        most_popular_table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="tabTrending"]/div[1]/div[2]')))

        list_columns = most_popular_table.find_elements_by_tag_name("div")

        for i in range(len(list_columns)):
            column = most_popular_table.find_element_by_xpath('.//div[' + str(i + 1) + ']/ul')
            rows = column.find_elements_by_tag_name("li")
            for j in range(len(rows)):
                cell = column.find_element_by_xpath('.//li[' + str(j + 1) + ']/a')
                make = cell.text
                url = cell.get_attribute("href")
                print(f"{make} - {url}")


if __name__ == '__main__':
    unittest.main()
