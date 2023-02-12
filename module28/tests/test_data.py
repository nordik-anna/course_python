from faker import Faker

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    first_name_1_char = 'А'
    first_name_31_char = 'Иваниваниваниваниваниваниванива'
    last_name_1_char = 'А'
    last_name_31_char = 'Ивановаааиааваииваавитиаваиаваиа'
    password_21_char = 'Phreefrhjlryyuuuuudbvh'
    password_no_Lower = 'qwertyu0'
    password_9_char = 'Qwertyu0p'
    password_not_contain_digit = "Qwertyui"
    xss = '<script>alert(123)</script>'
    email_without_domain = 'test@.ru'
    invalid_phoneNumber = '+71111111111'

class Valid_Data:
    valid_first_name = 'Анна'
    valid_last_name = 'Иванова'
    valid_password = 'Qwertyu0'
    valid_phoneNumber = '+79199684441'