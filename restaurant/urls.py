from django.urls import path, include
from . import views
from . import views_api

# There is another type of router called DefaultRouter which 
# provides an extra benefit over the SimpleRouter. 
# It creates an API root endpoint with a trailing slash that displays 
# all your API endpoints in one place. 
# You can use it this way in the urls.py file. 

from rest_framework.routers import DefaultRouter
router = DefaultRouter(trailing_slash=False)
router.register(r'users', views_api.UserViewSet, basename='users')
# urlpatterns += router.urls

urlpatterns = [
    path('home', views.index, name='home'),
    path('api/menu-items/', views_api.MenuItemsView.as_view()),
    path('api/menu-items/<int:pk>', views_api.SingleMenuItemView.as_view()),
    path('', include(router.urls)),
]



