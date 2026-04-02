from faker import Faker

# Создаем экземпляр с русской локалью
fake_ru = Faker('ru_RU')
fake_en = Faker('en_US')

def get_random_user():
    return {
        "full_name": fake_ru.name(),
        "phone_number": fake_en.phone_number(),
        "email": fake_en.email(),
        "comment": fake_ru.paragraph(3),
        "address": fake_ru.address()
    }

# Проверка функции get_random_user
if __name__ == "__main__":
    user = get_random_user()
    print(user)