from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("new_page",views.add,name="add"),
    path("random",views.random,name="random"),
    path("<str:title>",views.getClickedItem,name="description")
    
]
