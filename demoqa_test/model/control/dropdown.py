from selene.support.conditions import have
from selene.support.shared import browser


def select(selector, text):
    browser.element(selector).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(text)).click()