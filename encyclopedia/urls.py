from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("createnew/", views.createNew, name="createnew"),
    path('<str:title>/edit/', views.edit, name="edit"),
    path('random_page/', views.random_page, name="random_page"),

]
