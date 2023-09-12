from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title = "Pasta", price = 19.98, inventory = 6)
        self.assertEqual(item.__str__(), "Pasta : 19.98")
