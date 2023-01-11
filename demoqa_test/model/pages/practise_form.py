from selene.support.conditions import have
from selene.support.shared import browser
from demoqa_test.model.data.user import User

from demoqa_test.model.control import checkboxs, datapiecker, dropdown, radio_button
from demoqa_test.utils import upload



class PractiseFormPage:
    def __init__(self, user: User):
        self.user = user

    def fill_name(self):
        browser.element('#firstName').type(self.user.first_name)
        browser.element('#lastName').type(self.user.last_name)
        return self

    def fill_email(self):
        browser.element('#userEmail').type(self.user.email)
        return self

    def select_gender(self):
        radio_button.gender('[name=gender]', self.user.gender)
        return self

    def fill_phone_number(self):
        browser.element('#userNumber').type(self.user.number)
        return

    def click_databirthday(self):
        browser.element('#dateOfBirthInput').click()

    def select_month(self):
        browser.element('.react-datepicker__month-select').click()
        datapiecker.data_birthday('.react-datepicker__month-select', self.user.date_month)
        return self

    def select_year(self):
        browser.element('.react-datepicker__year-select').click()
        datapiecker.data_birthday('.react-datepicker__year-select', self.user.date_year)

    def select_day(self):
        browser.element(f'.react-datepicker__day--0{self.user.date_day}').click()
        return self

    def type_subject(self):
        browser.element('#subjectsInput').type(self.user.subjects).press_enter()
        return self

    def select_hobby(self):
        checkboxs.hobby('[for^="hobbies-checkbox"]', self.user.hobby)
        return self

    def upload_picture(self):
        upload.path_picture('#uploadPicture', self.user.picture)
        return self

    def select_state(self):
        dropdown.select('#state', self.user.state)
        return self

    def select_city(self):
        dropdown.select('#city', self.user.city)
        return self

    def type_address(self):
        browser.element('#currentAddress').type(self.user.address)
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def check_results(self):
        browser.all('.table-responsive td:nth-child(2)').should(have.texts(
            f'{self.user.first_name} {self.user.last_name}',
            self.user.email,
            self.user.gender,
            self.user.number,
            f'{self.user.date_day} {self.user.date_month} {self.user.date_year}',
            self.user.subjects,
            self.user.hobby,
            self.user.picture,
            self.user.address,
            f'{self.user.state} {self.user.city}'
        ))

    def open_registration_form(self):
        browser.open('/automation-practice-form')
        return self