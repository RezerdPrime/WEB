from django.test import TestCase
from .forms import LoginForm, RegisterForm
from articles.models import Yours_planet, Subb
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

class Testing(TestCase):

    @classmethod
    def setUpTestData(cls):
        ch = User.objects.create_user(
            username='chel1',
            password='123',
            email='chel1@gmail.com'
        )

        pl = Yours_planet.objects.create(
            planet='NEBIRU',
            user=ch
        )

        sb = Subb.objects.create(
            email=ch.email
        )


    def test_1(self): # Проверка на доступ к страницам
        a = self.client.get('/')
        self.assertEqual(a.status_code, 300)
        b = self.client.get('/articles/')
        self.assertEqual(b.status_code, 200)
        c = self.client.get('/articles/ToPD/')
        self.assertEqual(c.status_code, 200)


    def test_2(self): # Проверка обращения к объектам
        chel = User.objects.get(id=1)
        planet = Yours_planet.objects.get(id=1)

        print('\n\nFROM TEST2|\t' + chel.username + " " + planet.planet)
        print('\n\nFROM TEST2|\t')
        print(User.objects.all(), Yours_planet.objects.all())


    def test_3(self): # Проверка валидации подписки
        sub = Subb.objects.get(id=1)
        wrn_sub = Subb.objects.create(
            email='1325435'
        )
        #print(sub.email)
        try:
            validate_email(sub.email)
            print("\n\nFROM TEST3|\tВведенная строка является допустимым адресом электронной почты.")
        except ValidationError:
            print("\n\nFROM TEST3|\tВведенная строка не является допустимым адресом электронной почты.")

        try:
            validate_email(wrn_sub.email)
            print("\n\nFROM TEST3|\tВведенная строка является допустимым адресом электронной почты.")
        except ValidationError:
            print("\n\nFROM TEST3|\tВведенная строка не является допустимым адресом электронной почты.")


    def test_4(self): # проверка валидности формы логина с нормальными данным
        data = {
            'username': 'chelik',
            'password': '124342453dgsg35261',
            'email': 'chelik123@gmail.com'
        }
        log = LoginForm(data=data)
        self.assertFalse(log.is_valid())


    def test_5(self): # проверка валидности формы логина с неправильной почтой
        data = {
            'username': 'chelik',
            'password': '124342g35261',
            'email': 'ch123gmail.com'
        }
        log = LoginForm(data=data)
        self.assertFalse(log.is_valid())

    def test_6(self): # Проверка валидности формы регистрации с нормальными данными
        data = {
            'username': 'Test',
            'password': '123',
            'password_rep': '123',
            'email': 'dddl@gmail.com',
            'planet': 'Uran',
            'gender': '1',
            'opros': '',
        }
        reg = RegisterForm(data=data)
        self.assertFalse(reg.is_valid())


    def test_7(self): # Проверка валидности формы регистрации при не равных паролях
        data = {
            'username': 'Test',
            'password': '123',
            'password_rep': '33347',
            'email': 'dddl@gmail.com',
            'planet': 'Uran',
            'gender': '1',
            'opros': '',
        }
        reg = RegisterForm(data=data)
        self.assertFalse(reg.is_valid())


    def test_8(self): # Проверка валидности формы регистрации при индексе несуществующего гендера
        data = {
            'username': 'Test',
            'password': '123',
            'password_rep': '123',
            'email': 'dddl@gmail.com',
            'planet': 'q',
            'gender': '0',
            'opros': '',
        }
        reg = RegisterForm(data=data)
        self.assertFalse(reg.is_valid())

    def test_9(self): # Проверка валидности формы регистрации при нулевых данных
        data = {
            'username': 'Test',
            'password': '123',
            'password_rep': None,
            'email': 'dddl@gmail.com',
            'planet': 'q',
            'gender': '2',
            'opros': '',
        }
        reg = RegisterForm(data=data)
        self.assertFalse(reg.is_valid())


    def test_10(self): # Создание двух одинаковых юзеров
        user1 = User.objects.create_user(
            username='Eden Lichmer',
            password='dadadad',
            email='Lichmer@gmail.com'
        )

        try:
            user2 = User.objects.create_user(
                username='Eden Lichmer',
                password='dadadad',
                email='Lichmer@gmail.com'
            )
        except IntegrityError:
            print("\n\nFROM TEST10|\tЮзер уже существует.")


    def test_11(self): # Проверка на длину названия планеты
        user = User.objects.create_user(
            username='Eden Lichmer',
            password='dadadad',
            email='Lichmer@gmail.com'
        )

        planet1 = Yours_planet.objects.get(id=1)
        planet2 = Yours_planet.objects.create(
            planet='NEBIRUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU',
            user=user
        )

        self.assertEquals(len(planet2.planet), 20)


