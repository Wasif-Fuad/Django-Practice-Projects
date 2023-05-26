
from django.urls import path,include
from . import views
urlpatterns = [
    path('login/', views.log_in,name='login'),
    path('register/', views.register,name='register'),
    path('activate/<email_token>', views.activate,name='activate'),
]