from django.urls import path

from .views import StudentApiView

urlpatterns = [
    path('api', StudentApiView.as_view()),

]