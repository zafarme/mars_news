from django.urls import path
from .views import login_view,main_page

urlpatterns = [
    path('',view=main_page),
    path('login/', view=login_view,name='login')
]
