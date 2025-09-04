from faker import Faker


class GenerateData:

    fake_en = Faker('en_US')
    fake_ru = Faker('ru_RU')

#Генерация имени
    def create_name(self):
        return self.fake_ru.name()

#Генерация пароля
    def create_password(self):
        return self.fake_en.password()

#Генерация адреса
    def create_email(self):
        return self.fake_en.email()

#Генерация фамилии
    def create_last_name(self):
        return self.fake_ru.last_name()

#Генерация имени пользователя
    def create_user_name(self):
        return self.fake_en.word()