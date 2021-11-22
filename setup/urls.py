from django.contrib import admin
from django.urls import path
from rental_state.views import rental_state

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rental_state/', rental_state),
]
