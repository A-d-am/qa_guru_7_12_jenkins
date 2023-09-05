import selene
from selene import browser, have, be, command
from qa_guru_7_12_jenkins.models.users import User
from conftest import RESOURCES_DIR
import os
import allure


# noinspection PyMethodMayBeStatic
class RegistrationPage:

    def open(self):
        with allure.step('Открываем регистрационную форму'):
            browser.open('/automation-practice-form')

    def type_first_name(self, value):
        with allure.step(f'Вводим {value} в поле First Name'):
            browser.element('#firstName').should(be.blank).type(value)

    def type_last_name(self, value):
        with allure.step(f'Вводим {value} в поле Last Name'):
            browser.element('#lastName').should(be.blank).type(value)

    def type_email(self, value):
        with allure.step(f'Вводим {value} в поле Email'):
            browser.element('#userEmail').should(be.blank).type(value)

    def set_gender(self, value):
        with allure.step(f'Устанавливаем {value} в графе Gender'):
            browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def type_mobile(self, value):
        with allure.step(f'Вводим {value} в поле Mobile'):
            browser.element('#userNumber').should(be.blank).type(value)

    def type_subjects(self, values):
        with allure.step(f'Вводим {values} в поле Subjects'):
            for subject in values:
                browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()

    def set_date_of_birth(self, day, month, year):
        with allure.step(f'Выбираем день рождения пользователя: {day}.{month}.{year}'):
            browser.element('#dateOfBirthInput').click()
            browser.element(f".react-datepicker__month-select > option[value='{month - 1}']").click()
            browser.element(f".react-datepicker__year-select > option[value='{year}']").click()
            browser.element(f'.react-datepicker__day--0{day}').click()

    def set_hobbies(self, values):
        with allure.step(f'Выбираем хобби пользователя: {values}'):
            for hobby in values:
                browser.all('.custom-checkbox').element_by(have.exact_text(hobby)).click()

    def upload_picture(self, file_name):
        with allure.step(f'Загружаем картинку {file_name}'):
            file_path = os.path.join(RESOURCES_DIR, file_name)
            browser.element('#uploadPicture').send_keys(file_path)

    def type_current_address(self, value):
        with allure.step(f'Вводим {value} в поле Current Address'):
            browser.element('#currentAddress').should(be.blank).type(value)

    def set_state_and_city(self, state, city):
        with allure.step(f'Выбираем как {state} State и {city} как City'):
            browser.element('#state').perform(command.js.scroll_into_view).click()
            browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()

            browser.element('#city').perform(command.js.scroll_into_view).click()
            browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()

    def submit(self):
        with allure.step('Нажимаем на кнопку Submit'):
            browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_have_registered(self, user: User):
        with allure.step('Проверяем, что пользователь зарегистрирован и все данные успешно сохранены'):
            browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
            browser.element('.table').all('td').even.should(
                have.exact_texts(
                    f'{user.first_name} {user.last_name}',
                    user.email,
                    user.gender,
                    user.mobile,
                    user.get_full_birth_date(),
                    ', '.join(user.subjects),
                    ', '.join(user.hobbies),
                    user.picture,
                    user.current_address,
                    f'{user.state} {user.city}'
                )
            )
