
from generator import views
from django.urls import path

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("about", views.about, name="about"),
    path("", views.home, name="home"),
    path("generate-password", views.password, name="password"),
]
