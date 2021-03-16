# Create your views here.

from django.views.generic import TemplateView


class SMSView(TemplateView):
    template_name = "response.xml"
    content_type = "text/xml"
    def post(self, request, *args, **kwargs):
        context = dict()
        return self.render_to_response(context)
