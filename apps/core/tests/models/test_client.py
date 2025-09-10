import datetime
import unittest
import uuid

from apps.core.models.client import Gender, Client


# Test Case - Набір тестів
class ClientModelTests(unittest.TestCase):
    # Pre Condition - Запускається перед кожним методом тестом
    def setUp(self):
        self.client_data = {
            'surname': 'Smith',
            'name': 'John',
            'patronymic': 'Michaelson',
            'email': 'a@a.com',
            'birthday': datetime.date.fromisoformat('2005-05-15'),
            'gender': Gender.MALE,
            'uuid': uuid.uuid4(),
        }
        # Створення тестового об'єкту моделі перед кожним тестом
        # Створення об'єкту моделі, запис об'єкта в таблицю бази даних, присвоєння id об'єкту
        self.client = Client.objects.create(**self.client_data)

    # Test - Окремий тест
    # Перевірка чи правильно створився клієнт в таблиці
    def test_create_client(self):
        # Отримання об’єкту моделі із бази даних по id
        client = Client.objects.get(id=self.client.id)
        # Перевірка даних
        self.assertEqual(client.surname, self.client_data['surname'])
        self.assertEqual(client.name, self.client_data['name'])
        self.assertEqual(client.patronymic, self.client_data['patronymic'])
        self.assertEqual(client.email, self.client_data['email'])
        self.assertEqual(client.birthday, self.client_data['birthday'])
        self.assertEqual(client.gender, self.client_data['gender'])
        self.assertEqual(client.uuid, self.client_data['uuid'])

    def test_update_client(self):
        self.client.surname = "Johnson"
        self.client.name = "James"
        # ...
        # Обновлення даних моделі в базі
        self.client.save()
        # Перевірка чи дані правильно обновились
        updated_client = Client.objects.get(id=self.client.id)
        self.assertEqual(updated_client.surname, "Johnson")
        self.assertEqual(updated_client.name, "James")
        # ...

    def test_delete_client(self):
        client_id = self.client.id
        self.client.delete()
        with self.assertRaises(Client.DoesNotExist):
            Client.objects.get(id=client_id)

    # Post Condition - Запускається після кожного методу тесту
    def tearDown(self):
        # Видалення всіх записів із таблиці бази даних після виконання кожного тесту
        Client.objects.all().delete()
