from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create",views.create,name="create"),
    path("<int:listing_id>",views.listing_detail,name="listing_detail"),
    path("categories",views.categories,name="categories"),
    path("categories/<str:category_name>",views.category_name,name="category_name"),
    path("<int:listing_id>/remove",views.remove,name="remove"),
    path("<int:listing_id>/add",views.add,name="add"),
]
