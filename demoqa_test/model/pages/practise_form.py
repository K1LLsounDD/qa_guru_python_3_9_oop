from selene.support.conditions import have
from selene.support.shared import browser
from demoqa_test.model.data.user import User

from demoqa_test.model.control import checkboxs, datapiecker, dropdown, radio_button
from demoqa_test.utils import upload


class PractiseFormPage:
    def __init__(self):
        pass

    def fill_registration_fields(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        radio_button.gender('[name=gender]', user.gender)
        browser.element('#userNumber').type(user.number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        datapiecker.birthday('.react-datepicker__month-select', user.date_month)
        browser.element('.react-datepicker__year-select').click()
        datapiecker.birthday('.react-datepicker__year-select', user.date_year)
        browser.element(f'.react-datepicker__day--0{user.date_day}').click()
        browser.element('#subjectsInput').type(user.subjects).press_enter()
        checkboxs.hobby('[for^="hobbies-checkbox"]', user.hobby)
        upload.path_picture('#uploadPicture', user.picture)
        browser.element('#currentAddress').type(user.address)
        dropdown.select('#state', user.state)
        dropdown.select('#city', user.city)
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

    def open_registration_form(self):
        browser.open('/automation-practice-form')
        return self
