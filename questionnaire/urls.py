from django.urls import path

from questionnaire import views

urlpatterns = [
    path('create-survey', views.CreateSurveyView.as_view(), name='create-survey')
]
