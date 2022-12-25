from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, AdicionalViewSet


app_name = 'myapp'

router = DefaultRouter(trailing_slash=False)
router.register(r'itens', ItemViewSet)
router.register(r'adicionais', AdicionalViewSet)

urlpatterns = router.urls