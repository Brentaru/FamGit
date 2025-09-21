from django.urls import path
from . import views

app_name = "Reserves"

urlpatterns = [
    path("", views.home, name="home"),          # GET /
    path("home/", views.home, name="home_url"), # GET /home/
    # optional: if you really want /Reserves/
    path("Reserves/", views.home, name="home_alias"),
    path("detail/<int:pk>/", views.detail, name="detail"), # GET /detail/1/
]
