from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import  UsersViewset

class CustomRouter(DefaultRouter):
      """
      Custom router to filter out unwanted URLs as no need for list and create actions.
      """
      def get_urls(self):
            urls = super().get_urls()

            # Filter out unwanted URLs
            filtered_urls = []
            for url in urls:
                  if not any(action in url.name for action in ["list", "create"]):
                        filtered_urls.append(url)

            return filtered_urls



routers = CustomRouter()
routers.register(r"users", UsersViewset, basename="users")

urlpatterns = [
      path("", include(routers.urls))
]
