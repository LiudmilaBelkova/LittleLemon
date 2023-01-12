from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APIClient

import json
from restaurant.models import Menu
from restaurant.views_api import MenuItemsView
from rest_framework.test import force_authenticate


class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.user.save()
        token = Token.objects.create(user=self.user)
        token.save()

        number_of_menus = 8
        for menu_id in range(number_of_menus):
            Menu.objects.create(
                title=f"Menu item {menu_id}",
                price=f"{menu_id * 2}",
                inventory=f"{menu_id * 3}",
            )
        

    def test_get_all(self):
        self.client.login(username='test', password='test')
        #raise Exception(self.client.login(username='test', password='test'))
        response = self.client.get("/api/menu-items")
        #raise Exception(response)
        menus = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(menus["results"]), 8)
    