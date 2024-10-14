from django.urls import path, include
from . import views
from django.contrib import admin


# Define your app's URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hospital/', include('Hospital.urls.py'))]