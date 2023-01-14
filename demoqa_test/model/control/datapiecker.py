from selene.support.conditions import have
from selene.support.shared import browser


def birthday(selector, value):
    browser.element(selector).all('option').element_by(have.exact_text(value)).click()
