from django.urls import path, re_path
from . import views

urlpatterns=[
    re_path('addcountry',views.add_country),
]