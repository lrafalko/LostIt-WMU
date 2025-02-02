
import django.urls
from django.urls import path
from . import views

urlpatterns = [
    path('createLostItem/', view=views.createLostItem.as_view()),
    path('removeLostItem/', view=views.deleteLostItem.as_view())
]