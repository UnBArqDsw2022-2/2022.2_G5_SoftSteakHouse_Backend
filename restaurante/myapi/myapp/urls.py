from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, AdicionalViewSet, MesaViewSet


app_name = 'myapp'

router = DefaultRouter(trailing_slash=False)
router.register(r'itens', ItemViewSet)
router.register(r'adicionais', AdicionalViewSet)
router.register(r'mesas', MesaViewSet)

urlpatterns = router.urls