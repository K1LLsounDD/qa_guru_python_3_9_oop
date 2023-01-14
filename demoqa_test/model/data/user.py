from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    date_year: str
    date_month: str
    date_day: int
    subjects: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


#Sergey_user = User(
#    first_name='Sergey',
#    last_name='QA',
#    email='example@pochta.com',
#    gender='Male',
#    number='8800553555',
#    date_year='1999',
#    date_month='July',
#    date_day=11,
#    subjects='Economics',
#    hobby='Sports',
#    picture='picture/stich.jpg',
#    address='street Pushkina, home 5',
#    state='NCR',
#    city='Delhi')
