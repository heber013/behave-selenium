from behave import step

from constants.page_mappings import pages


@step(u'I go to "{url}"')
def go_to_page(context, url):
    """
    Navigate the the given url.
    The corresponding page object instance is stored in context
    variable: current_page
    :param url: the url to navigate to
    """
    if url in pages.keys():
        context.browser.get(url)
        context.current_page = pages[url](context.browser)
    else:
        raise Exception(
            'Url %s is not present in pages mapping: %s' % (url, pages))


@step(u'I am on "{page}" Page')
def check_page(context, page):
    """
    Check if the given page is the one that is open in the browser
    :param page: the page to check. Can be the page title or the url.
    """
    assert page in context.browser.title or page in context.browser.current_url, \
        'Pages do not match. Actual: %s. Expected: %s' % (
            context.browser.title, page)
