from django.conf.urls import url
from e_cloud_finance_module import views
# SET THE NAMESPACE!
app_name = 'e_cloud_finance_module'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'user_login/$',views.user_login,name='user_login'),
     url(r'contacts/$',views.contacts,name='contacts'),
]
