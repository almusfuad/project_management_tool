from django.urls import path
from tasks.views import TaskViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"tasks", TaskViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = router.urls