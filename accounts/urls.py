from django.urls import path
from .import views
urlpatterns = [
   path('signup/', views.Signup, name='signup'),
   path('login/', views.Login, name='login'),
   path('logout/', views.Logout, name='logout'),

]