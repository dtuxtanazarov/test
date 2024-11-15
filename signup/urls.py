from django.urls import path
from .views import *


urlpatterns=[
    path('logout', logout_user, name='logout'),
    path('', SignUP.as_view(), name='signup'),

]