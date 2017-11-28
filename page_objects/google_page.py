from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_objects.base_page import BasePage

search_box = (By.ID, 'lst-ib')
results = (By.CLASS_NAME, 'rc')


class GooglePage(BasePage):

    def write_in_search_box(self, text):
        self.find_element(search_box).send_keys(text)
        return self

    def press_key_in_searchbox(self, key):
        self.find_element(search_box).send_keys(getattr(Keys, key))
        return self

    def click_on_link(self, link):
        from constants.page_mappings import pages
        links = self.find_elements(results)
        for _link in links:
                url = _link.find_element(By.TAG_NAME, 'cite').text
                print(url)
                if url == link:
                    _link.find_element(By.TAG_NAME, 'a').click()
                return pages[link](self.driver)
        raise Exception('Link %s not found' % link)

    def click_on_link_by_link_text(self, link):
        self.find_element((By.LINK_TEXT, link)).click()
