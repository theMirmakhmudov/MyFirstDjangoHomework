from django.urls import path
from apps.views import main, team

urlpatterns = [
    path("home", main, name="main"),
    path("team", team, name="team")
]
