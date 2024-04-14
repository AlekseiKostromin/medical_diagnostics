from django.contrib.auth import get_user_model
from django.test import TestCase
from main.models import LabTest, TestCategory
from cart.models import Cart, CartItem
from users.models import User

user = get_user_model()
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
        self.client.force_login(self.user)

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

        self.cart = Cart.objects.create(
            user=self.user,
        )

        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            labtest=self.labtest,
            quantity=1,
            price=200
        )

    def test_cart(self):

        response = self.client.get('/cart/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart_list.html')
