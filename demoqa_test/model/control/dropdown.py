from selene.support.conditions import have
from selene.support.shared import browser


class Dropdown:
    def __init__(self, selector):
        self.selector = selector

    def select(self, text):
        browser.element(self.selector).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(text)).click()
        return self
