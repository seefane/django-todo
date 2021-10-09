from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('registration/',views.ApiCreateTask.as_view(),name='registration'),
    path('login/',obtain_auth_token,name='login'),

]