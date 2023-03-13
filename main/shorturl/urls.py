from django.urls import path
from shorturl import views

app_name = 'shorturl'

urlpatterns = [
    path('make/', views.ShortView.as_view(), name='make'),
    path('result/', views.ResultView.as_view(), name='result'),

]
