from django.urls import path
from .views import home, chart_1

urlpatterns = [
    path('', home, name="home"),
    path('chart_1/', chart_1, name="chart_1")
]