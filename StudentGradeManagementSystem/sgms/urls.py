from django.urls import path
from django.contrib import admin
from .views import register, add_attendance, add_grade, home, register, user_login, user_logout, view_attendance, view_grades

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register, name='register'),
    path('login/', user_login, name='login'),
    path('add_grade/', add_grade, name='add_grade'),
    path('view_grades/', view_grades, name='view_grades'),
    path('add_attendance/', add_attendance, name='add_attendance'),
    path('view_attendance/', view_attendance, name='view_attendance'),
    path('logout/', user_logout, name='logout'),
    path('home', home, name='home'),
]