from rest_framework.routers import DefaultRouter

from entities.views import EntityViewSet


app_name = "entities"

router = DefaultRouter()
router.register("entities", EntityViewSet, basename="entity")

urlpatterns = router.urls
