from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include,path

router = DefaultRouter()
router.register(r'users', views.RegisterUser, basename="users")


urlpatterns = [
    url('',include(router.urls)),
    # path('user/me',views.LoginUserView.as_view())
]