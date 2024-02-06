
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app1.views import *
from app2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include("app1.urls")),
    path('app2/', include("app2.urls"))
]
