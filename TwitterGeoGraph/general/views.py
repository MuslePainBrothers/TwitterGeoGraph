from django.views import generic


class TopView(generic.TemplateView):
    template_name = "top.html"


class IndexView(generic.TemplateView):
    template_name = "index.html"
