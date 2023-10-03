
from django.contrib import admin
from django.urls import path,include
from djangoapp.views import getConnection

from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djangoapp.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs", SpectacularSwaggerView.as_view(url_name="schema") ),
    path('', getConnection),
]
