from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # /admin/
    path("admin/", admin.site.urls),
    # /webapp/
    path("", include("webapp.urls")),
    # /accounts/
    path("accounts/", include("accounts.urls")),
    # /bands/
    path("bands/", include("bands.urls")),
]
