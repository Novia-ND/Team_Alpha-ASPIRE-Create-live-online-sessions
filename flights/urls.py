from django.urls import path
from flights import views

app_name = 'flights'
urlpatterns = [
    path('',views.home, name = 'home'),
    path('login',views.login, name = 'login'),
    path('home/<str:name>',views.home1, name = 'home1'),
    path('forum/<str:name>',views.forum, name = 'forum'),
    path('notes/<str:name>',views.notes, name = 'notes'),
    path('course/<str:foo>',views.course, name = 'course'),
    path('userlogin',views.userlogin, name = 'userlogin'),
    path('usersignin',views.usersignin, name = 'usersignin'),
    path('teacherlogin',views.teacherlogin, name = 'teacherlogin'),
    path('teachersignin',views.teachersignin, name = 'teachersignin'),
    path('course',views.course, name = 'flights'),
    path('download',views.download, name = 'download'),
    path('upcoming/<str:name>/<str:sub>',views.upcoming, name = 'upcoming'),
    path('popular/<str:name>',views.popular, name = 'popular'),
    path('thisweek/<str:name>',views.thisweek, name = 'thisweek'),
    path('profile/<str:foo>',views.profile, name = 'profile'),
    path('live/<str:name>/<str:sub>',views.live, name = 'live'),
    path('select',views.select, name = 'select'),
    path('select1',views.select1, name = 'select1'),
]