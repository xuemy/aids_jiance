from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from .models import Shizhi, Questions


def index(request):
    # 试纸首页，试纸套装
    return render(request, 'shizhi/index.html')

class IntroView(DetailView):
    model = Shizhi
    template_name = 'shizhi/intro.html'
    slug_url_kwarg = 'bianhao'
    slug_field = 'bianhao'


class QuestionsView(ListView):
    model = Questions
    template_name = 'shizhi/questions.html'
    paginate_by = 15



    def get_queryset(self):
        shizhi = get_object_or_404(Shizhi, bianhao=self.kwargs.get('bianhao'))
        setattr(self, 'shizhi', shizhi)
        return super(QuestionsView, self).get_queryset().filter(shizhi=shizhi)

    def get_context_data(self, **kwargs):
        context = super(QuestionsView, self).get_context_data(**kwargs)
        context['shizhi'] = self.shizhi
        return context
