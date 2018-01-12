from django.conf.urls import url

from aids_jiance.shizhi import views

urlpatterns = [
    url(regex=r'^$', view=views.index, name='shizhi'),
    url(regex=r'^(?P<bianhao>\w+)$', view=views.IntroView.as_view(), name='shizhi_intro'),
    url(regex=r'^(?P<bianhao>\w+)/questions/$', view=views.QuestionsView.as_view(), name='shizhi_questions')
]
