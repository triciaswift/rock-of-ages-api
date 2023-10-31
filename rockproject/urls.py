from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rockapi.views import register_user, login_user, TypeView, RockView

router = routers.DefaultRouter(
    trailing_slash=False
)  # Tells router to accept /types instead of /types/
router.register(
    r"types", TypeView, "type"
)  # r'types' is setting up the URL, TypeView is telling the server which view to use when it sees that URL, 'type' is called the base name which you'll only see if you get an error (usually singular version of the URL)
router.register(r"rocks", RockView, "rock")

urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("admin/", admin.site.urls),
]
