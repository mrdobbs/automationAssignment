import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LevelsBeyondSearch(unittest.TestCase):

	def setUp(self):
        	self.driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.

	def test_levels_beyond_google_search_result(self):
		driver = self.driver
		driver.get('http://www.google.com/')
		time.sleep(1)
		search_box = driver.find_element_by_name('q')
		search_box.send_keys('reach levels beyond engine')
		search_box.submit()
		
		time.sleep(5) 					#sleep so the results can load and the user can see what is happening
		RESULTS_LOCATOR = "//div/h3/a"
		time.sleep(1)
		page1_results = driver.find_element_by_xpath(RESULTS_LOCATOR)
		assert "Levels Beyond" in page1_results.text
		print( "Success: www.reachengine.com was the first search result")
		page1_results.click()
		time.sleep(10)

		mailto = driver.find_element_by_id("et-info-email")
		assert "mailto:demo@reachengine.com" in mailto.get_attribute("href")
		print( "Success: contact info is listed on the homepage")

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()