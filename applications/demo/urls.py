from django.conf.urls import url

from applications.demo import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
]
