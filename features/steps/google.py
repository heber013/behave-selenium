from behave import step


@step(u'I type "{text}" in the searchbox')
def type_in_search_box(context, text):
    """
    Write the given text in the search box
    :param text: the string to write in the search box
    """
    context.current_page = context.current_page.write_in_search_box(text)


@step(u'I press "{key}" in the searchbox')
def type_in_search_box(context, key):
    """
    Press a key in the search box
    :param key: the string representing the key to press.
    Example: 'ENTER'. FOr reference see: selenium.webdriver.common.keys
    """
    context.current_page = context.current_page.press_key_in_searchbox(key)


@step(u'I click on "{link}" link')
def type_in_search_box(context, link):
    """
    Click link on the page that exact matches the given one
    :param link: the link to be clicked on
    """
    context.current_page = context.current_page.click_on_link(link)


@step(u'I click on "{link}" by link text')
def type_in_search_box(context, link):
    """
    Click on a link by its link text
    :param link: the link text to be clicked on
    """
    context.current_page = context.current_page.click_on_link_by_link_text(link)
