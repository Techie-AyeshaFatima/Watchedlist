from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("search", views.search, name="search"),
    path('item/<str:id>/', views.item, name='item'),
    path('update_list/<str:id>/', views.update_list, name='update_list'),
    path("mylist", views.mylist, name="mylist"),
    path("watched", views.watched, name="watched"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("dropped", views.dropped, name="dropped"),
]
