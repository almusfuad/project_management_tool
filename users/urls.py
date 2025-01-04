from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import  UsersViewset



routers = DefaultRouter()
routers.register(r"users", UsersViewset, basename="users")

urlpatterns = [
      path("", include(routers.urls))
]
