from rest_framework.routers import DefaultRouter
from .views import ItemViewSet


app_name = 'myapp'

router = DefaultRouter(trailing_slash=False)
router.register(r'itens', ItemViewSet)

urlpatterns = router.urls