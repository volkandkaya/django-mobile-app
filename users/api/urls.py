from django.conf.urls import url

from .views import MeApiHandler

urlpatterns = [
    url(r"^me$", MeApiHandler.as_view()),
]
