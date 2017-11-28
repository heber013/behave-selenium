from page_objects.google_page import GooglePage
from page_objects.selenium_page import SeleniumPage

"""
Contains the mapping between urls and the corresponding page class.
"""

pages = {
    'http://www.google.com': GooglePage,
    'www.seleniumhq.org/': SeleniumPage
}
