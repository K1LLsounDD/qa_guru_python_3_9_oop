from selene.support.shared import browser

from demoqa_test.model.pages.practise_form import PractiseFormPage
from demoqa_test.model.data.user import User

#browser.config.hold_browser_open = True
practise_form = PractiseFormPage()


def test_form_registration():
    user = User(first_name='Sergey',
                last_name='QA',
                email='example@pochta.com',
                gender='Male',
                number='8800553555',
                date_year='1999',
                date_month='July',
                date_day=11,
                subjects='Maths',
                hobby='Music',
                picture='picture/stich.jpg',
                address='street Pushkina, home 5',
                state='NCR',
                city='Delhi')

    practise_form.open_registration_form()
    practise_form.fill_registration_fields(user).submit()

    practise_form.check_results(user)