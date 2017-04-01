from django.views import generic
from django.conf import settings


class TopView(generic.TemplateView):
    template_name = "top.html"

    def get_context_data(self, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        context["key"] = settings.GOOGLE_API_KEY
        return context


class IndexView(generic.TemplateView):
    template_name = "index.html"
