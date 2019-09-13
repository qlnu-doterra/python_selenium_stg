import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):
    """This challenge requires listing of most popular items"""

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("../drivers/chromedriver")

    def tearDown(self) -> None:
        self.driver.close()

    def test_challenge1(self):
        # launch the site
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart USA", self.driver.title)

        self.driver.maximize_window()






        # exotic search page
        self.driver.find_element_by_link_text("Exotics").click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="mainBody"]/div[1]/div/div[1]/div[1]/div/div[2]/div[3]/h1/span[2]')))
        text = element.text
        self.assertIn("exotic".lower(), str(text).lower())

        # validate Porsche is listed
        list_of_car = list()
        table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr')))
        tableRows = self.driver.find_elements_by_xpath('//*[@id="serverSideDataTable"]/tbody/tr')
        for i in range(len(tableRows)):
            car_make = self.driver.find_element_by_xpath(
                '//*[@id="serverSideDataTable"]/tbody/tr[' + str(i + 1) + ']/td[5]/span').text
            list_of_car.append(car_make)
        self.assertTrue("PORSCHE" in list_of_car, "Porsche is not listed")


if __name__ == '__main__':
    unittest.main()