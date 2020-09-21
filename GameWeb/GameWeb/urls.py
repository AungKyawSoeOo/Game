"""GameWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import gen.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',gen.views.home,name='home'),
    path('action',gen.views.action,name='action'),
    path('adventure',gen.views.adventure,name='adventure'),
    path('role',gen.views.role,name='role'),
    path('sport',gen.views.sport,name='sport'),
    path('action/<int:action_id>',gen.views.acdetail,name='acdetail'),
    path('adventure/<int:adventure_id>', gen.views.avdetail, name='avdetail'),
    path('role/<int:role_id>', gen.views.roledetail, name='roledetail'),
    path('sport/<int:sport_id>', gen.views.sportdetail, name='sportdetail'),

]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)