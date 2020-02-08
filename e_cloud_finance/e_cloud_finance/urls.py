from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from e_cloud_finance_module import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'index',views.index,name='index'),
    url(r'special/',views.special,name='special'),
    url(r'e_cloud_finance_module/',include('e_cloud_finance_module.urls')),
    url(r'logout/$', views.user_logout, name='logout'),
]
