from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from student_management_system import settings

from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairCustomView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("api/v1/student_management/", include("student_management_app.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/",
        MyTokenObtainPairCustomView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
     path('', include('student_management_app.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






