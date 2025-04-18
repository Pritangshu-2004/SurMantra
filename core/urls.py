from django.urls import path
from . import views  # Import views from the same app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),          # URL: /
    path('about/', views.about, name='about'),  # URL: /about/
    path('showcase/', views.showcase, name='showcase'),  # URL: /showcase/
    path('blog/', views.blog, name='blog'),  # URL: /blog/
    path('blog/create/', views.blog_create, name='blog_create'),  # URL: /blog/create/
    path('blog/<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('blog/delete/<int:pk>/', views.blog_delete, name='blog_delete'),  # URL: /blog/delete/<pk>/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files
