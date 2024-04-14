from django.test import TestCase
from main.models import LabTest, TestCategory
from users.models import User


class TestMain(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@yandex.ru',
            first_name='Aleksei',
            last_name='Aleksei',
            password='a3499765',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        self.testcategory = TestCategory.objects.create(
            name='Category',
        )

        self.labtest = LabTest.objects.create(
            name='test',
            category=self.testcategory,
            description='test',
            price=1000,
            time=2,
        )

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contacts.html')

    def test_labtest_list(self):
        response = self.client.get('/labtest_list')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/labtest_list.html')

    def test_doctor_list(self):
        response = self.client.get('/doctor_list')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/doctor_list.html')

    def test_create_labtest(self):
        data = {
            'name': 'test1',
            'category': self.testcategory,
            'description': 'test1',
            'price': 2000,
            'time': 4,
        }
        response = self.client.post(
            '/labtest_create/',
            data=data
        )

        self.assertEqual(response.status_code, 200)
