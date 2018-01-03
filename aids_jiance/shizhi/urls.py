from django.conf.urls import url

from aids_jiance.shizhi import views

urlpatterns = [
    url(regex=r'^$', view=views.index, name='shizhi'),
    url(regex=r'^shiyong$', view=views.ShizhiShiyongView.as_view(), name='shizhi_shiyong'),
    url(regex=r'^(?P<slug>\w+)$', view=views.IntroView.as_view(), name='shizhi_intro'),
    url(regex=r'^(?P<slug>\w+)/questions/$', view=views.QuestionsView.as_view(), name='shizhi_questions')
]
