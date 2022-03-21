from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'employees/', views.employeeList.as_view()),
]
