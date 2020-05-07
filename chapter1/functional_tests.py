from selenium import webdriver

import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Visit the homepage
        self.browser.get('http://localhost:8000')
        
        # Notices the page title and header mention to-do lists
        self.assertIn('To-Do lists', self.browser.title)
        self.fail('Finish the test!')



        # invited to add todo item


if __name__=='__main__':
    unittest.main()

