from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from e_cloud_finance_module import views
from django.conf.urls.static import static
from django.conf import settings
from e_cloud_finance_module.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',views.index,name='index'),
    url(r'special/',views.special,name='special'),
    # url(r'e_cloud_finance_module/',include('e_cloud_finance_module.urls')),
    url(r'logout/$', views.user_logout, name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'user_login/$',views.user_login,name='user_login'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
