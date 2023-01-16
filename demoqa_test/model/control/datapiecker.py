from selene.support.conditions import have
from selene.support.shared import browser


class DatePiecker:
    def __init__(self, selector):
        self.selector = selector

    def birthday(self, value):
        browser.element(self.selector).all('option').element_by(have.exact_text(value)).click()
        return self
