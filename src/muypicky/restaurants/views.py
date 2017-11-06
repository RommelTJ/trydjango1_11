import random
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        num = random.randint(0, 1000)
        some_list = [
            random.randint(0, 1000),
            random.randint(0, 1000),
            random.randint(0, 1000)
        ]
        context = {
            "num": num,
            "some_list": some_list
        }
        return context

