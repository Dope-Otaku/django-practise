
from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include("app1.urls")),
    path('app2/', include("app2.urls")),
    path('todoapp/', include("todoapp.urls"))
]
