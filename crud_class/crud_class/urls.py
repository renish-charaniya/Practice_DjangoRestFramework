
from django.contrib import admin
from django.urls import path
from django.utils.decorators import method_decorator
from crud_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentAPI.as_view()),
]
