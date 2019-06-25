from django.urls import path
from .import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('mybooks/', views.UserBooks, name='mybooks'),
    path('detail/<slug:book_slug>/', views.Detail,name='detail'),
    path('search/',views.Search,name='search'),
    path('upload/', views.AddBook, name='add'),
    path('edit/<slug:slug>/',views.EditBook,name='edit'),
    path('delete/<slug:slug>', views.DeleteBook, name='delete'),
    path('deletecomment/<int:id>', views.DeleteComment, name='deletecmnt'),
]