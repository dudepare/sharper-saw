import unittest
from selenium import webdriver


class CountFilled(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def test_count_filled(self):
        self.driver.get("http://apply.dataprocessors.com.au/")
        self.driver.find_element_by_css_selector(
            "html body form p input[name='jobref']").send_keys("PO65")
        filled = self.driver.find_elements_by_css_selector("html body form p img[src='filled_O.gif']")
        self.driver.find_element_by_css_selector(
            "html body form p input[name='value']").send_keys(
            "{}".format(len(filled)))
        self.driver.find_element_by_css_selector(
            "html body form p input[value='Submit']").click()

    def tearDown(self):
        print(self.driver.page_source)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
