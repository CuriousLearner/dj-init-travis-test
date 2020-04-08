# Third Party Stuff
from rest_framework.routers import DefaultRouter

# dj-init-travis-test Stuff
from dj_init_travis_test.base.api.routers import SingletonRouter
from dj_init_travis_test.users.api import CurrentUserViewSet
from dj_init_travis_test.users.auth.api import AuthViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register("auth", AuthViewSet, basename="auth")
singleton_router.register("me", CurrentUserViewSet, basename="me")

# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls
