from django.views import generic
from django.conf import settings
from django.shortcuts import redirect


class TopView(generic.TemplateView):
    template_name = "top.html"


class MapView(generic.TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context["key"] = settings.GOOGLE_API_KEY
        return context


class IndexView(generic.TemplateView):
    template_name = "index.html"


def clawlerTwitter(request):
    # ここでtwitter認証したuserのaccess_tokenを用いて、tweepyを使用してクロールする
    # python_social_authモデルのuser_social_authsを取りたい
    #
    # （保留）
    #
    user = request.user
    print(user)
    return redirect('general:index')
