from django.conf.urls import patterns, include, url
from django.contrib import admin

from bhive_app import views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/questions/', views.QuestionsList.as_view()),
    url(r'^api/questions/(?P<pk>[0-9]+)/', views.QuestionsDetail.as_view()),
    url(r'^api/answers/(?P<pk>[0-9]+)/', views.AnswerVote.as_view()),
)
