# Create your views here.
from django.views.generic.base import TemplateView

# TemplateView


class HomeView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context
