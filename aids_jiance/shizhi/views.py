from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from .models import Shizhi, Questions


def index(request):
    return render(request, 'shizhi/index.html')


class ShizhiShiyongView(TemplateView):
    template_name = 'shizhi/shiyong.html'


class IntroView(DetailView):
    model = Shizhi
    template_name = 'shizhi/intro.html'


class QuestionsView(ListView):
    model = Questions
    template_name = 'shizhi/questions.html'
    paginate_by = 15



    def get_queryset(self):
        shizhi = get_object_or_404(Shizhi, slug=self.kwargs.get('slug'))
        setattr(self, 'shizhi', shizhi)
        return super(QuestionsView, self).get_queryset().filter(shizhi=shizhi)

    def get_context_data(self, **kwargs):
        context = super(QuestionsView, self).get_context_data(**kwargs)
        context['shizhi'] = self.shizhi
        return context
