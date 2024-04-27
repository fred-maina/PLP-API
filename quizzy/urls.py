from django.urls import path
from . import views
urlpatterns=[
path("",views.index,name="index"),
path("questions", views.index,name="questions"),
path("quiz",views.quiz,name="quiz"),
path("results",views.finalscore,name="finalscore")
]