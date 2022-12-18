from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
  path('api/v1/', include('myapp.urls', namespace='myapp')),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # retirar caso de problema
  path('token/', TokenObtainPairView.as_view()),
  path('token/refresh/', TokenRefreshView.as_view()),
  path('admin/', admin.site.urls),
]