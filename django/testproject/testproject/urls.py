from django.contrib import admin
from django.urls import include, path
from app.views import DepartmentViewSet, StudentViewSet
from app.views import CustomTokenObtainPairView
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view



schema_view = get_swagger_view(title='API Documentation')
router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
    path('api/docs/', schema_view),

]
