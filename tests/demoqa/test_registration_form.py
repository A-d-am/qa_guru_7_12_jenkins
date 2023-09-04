import allure
from qa_guru_7_12_jenkins.pages.registration_page import RegistrationPage
import pytest
from qa_guru_7_12_jenkins.models.users import User


@pytest.fixture()
def user_to_test():
    user_to_test = User(
        first_name='FirstName',
        last_name='LastName',
        email='username@domain.com',
        gender='Male',
        mobile='1234567890',
        date_of_birth_day=17,
        date_of_birth_month=4,
        date_of_birth_year=2000,
        subjects=['Maths', 'Hindi'],
        hobbies=['Sports'],
        picture='test_pict.png',
        current_address='Current address',
        state='NCR',
        city='Delhi'
    )
    return user_to_test


@allure.title("Successful fill form")
def test_successful(setup_browser, user_to_test):
    registration_page = RegistrationPage(setup_browser)
    registration_page.open()

    # Name
    registration_page.type_first_name(user_to_test.first_name)
    registration_page.type_last_name(user_to_test.last_name)

    # Email
    registration_page.type_email(user_to_test.email)

    # Gender
    registration_page.set_gender(user_to_test.gender)

    # Mobile
    registration_page.type_mobile(user_to_test.mobile)

    # Date of birth
    registration_page.set_date_of_birth(user_to_test.date_of_birth_day, user_to_test.date_of_birth_month,
                                        user_to_test.date_of_birth_year)

    # Subjects
    registration_page.type_subjects(user_to_test.subjects)

    # Hobbies
    registration_page.set_hobbies(user_to_test.hobbies)

    # Picture
    registration_page.upload_picture(user_to_test.picture)

    # Current Address
    registration_page.type_current_address(user_to_test.current_address)

    # State and City
    registration_page.set_state_and_city(user_to_test.state, user_to_test.city)

    # Click on submit button
    registration_page.submit()

    # Check registered user info
    registration_page.should_have_registered(user_to_test)
