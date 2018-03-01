from selenium import webdriver


def before_all(context):
    capabilities = webdriver.DesiredCapabilities.CHROME
    context.browser = webdriver.Remote('http://localhost:4444/wd/hub',
                                       desired_capabilities=capabilities)


def after_all(context):
    context.browser.quit()
