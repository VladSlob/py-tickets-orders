from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import OrderViewSet

app_name = "cinema"  # Add this line

router = DefaultRouter()
router.register(r"orders", OrderViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls)),
]
