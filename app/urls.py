from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'items', views.ItemViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register', views.registerpage, name='register'),
    path('login', views.LoginView, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index', views.index, name='index'),
    path('add_item', views.add_item, name='add_item'),
    path('delete_item/<str:id>/', views.delete_item, name='delete_item'),
    path('finished_status/<str:id>/', views.finished_status, name='finished_status'),
]