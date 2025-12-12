from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),

    # DRF API routes
    path("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
]

