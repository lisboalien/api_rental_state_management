from django.contrib import admin
from django.urls import path, include
from rental_state.views import RentalStateViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('rental_state', RentalStateViewSet, basename='RentalState')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
