# MultipleFiles/urls.py
from django.urls import path
from .views import register, login_view, logout_view, contact, profile, delete_account

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contact/', contact, name='contact'),  # Uncomment if you have a contact view
    # path('update-profile/', update_profile, name='update_profile'),
    path('delete_account/', delete_account, name='delete_account'),
    path('profile/', profile, name='profile')
]
