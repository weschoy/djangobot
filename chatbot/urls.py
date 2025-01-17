from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^sms/', include('sms.urls')),
]