from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="TestMenuItem", price=10.05, inventory=80)
        #raise Exception(str(item))
        self.assertEqual(str(item), "TestMenuItem : 10.05 : 80")

# to test run python manage.py test
