from django.contrib import admin
from django.urls import path
# Use include() to add paths from the e_cloud_finance_module application
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


# def trigger_error(request):
#     division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('e_cloud_finance_module/', include('e_cloud_finance_module.urls')),
    # path('sentry-debug/', trigger_error),
    path('', RedirectView.as_view(url='/e_cloud_finance_module/', permanent=True)),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
