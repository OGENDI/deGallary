from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='about'),
    path('photos/', views.photos, name ='photos'),
    path('search/', views.search, name='search'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)