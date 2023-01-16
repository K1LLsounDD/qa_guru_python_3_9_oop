from selene.support.conditions import have
from selene.support.shared import browser
from demoqa_test.model.data.user import User

from demoqa_test.model.control.checkboxs import Checkbox
from demoqa_test.model.control.dropdown import Dropdown
from demoqa_test.model.control.radio_button import RadioButton
from demoqa_test.model.control.datapiecker import DatePiecker
from demoqa_test.utils import upload


class PractiseFormPage:
    def __init__(self):
        pass

    def fill_registration_fields(self, user: User):
        checkbox = Checkbox(browser.all('[for^="hobbies-checkbox"]'))
        dropdown_state = Dropdown('#state')
        dropdown_city = Dropdown('#city')
        button = RadioButton('[name=gender]')
        datepiecker_month = DatePiecker('.react-datepicker__month-select')
        datepiecker_year = DatePiecker('.react-datepicker__year-select')

        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        button.gender(user.gender)
        browser.element('#userNumber').type(user.number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        datepiecker_month.birthday(user.date_month)
        browser.element('.react-datepicker__year-select').click()
        datepiecker_year.birthday(user.date_year)
        browser.element(f'.react-datepicker__day--0{user.date_day}').click()
        browser.element('#subjectsInput').type(user.subjects).press_enter()
        checkbox.hobby(user.hobby)
        upload.path_picture('#uploadPicture', user.picture)
        browser.element('#currentAddress').type(user.address)
        dropdown_state.select(user.state)
        dropdown_city.select(user.city)
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def check_results(self, user: User):
        browser.all('.table-responsive td:nth-child(2)').should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.number,
            f'{user.date_day} {user.date_month},{user.date_year}',
            user.subjects,
            user.hobby,
            user.picture.split('/')[-1],
            user.address,
            f'{user.state} {user.city}'
        ))
        return self

    def open_registration_form(self):
        browser.open('/automation-practice-form')
        return self
