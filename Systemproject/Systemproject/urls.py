from django.contrib import admin
from django.urls import path, include


# Define your app's URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Hospital.urls'))
]