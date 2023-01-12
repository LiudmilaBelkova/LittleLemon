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
router.register(r'bookings', views_api.BookingViewSet)


urlpatterns = [
    # HTML pages
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings', views.bookings, name='bookings'),

    # API endpoints
    path('api/menu-items/', views_api.MenuItemsView.as_view()),
    path('api/menu-items/<int:pk>', views_api.SingleMenuItemView.as_view()),
    path('api/', include(router.urls)),
      
]



