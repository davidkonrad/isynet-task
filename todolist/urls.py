from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tasks/', views.tasks),
 		path('item/<int:item_id>/', views.item),
 		path('solve/<int:item_id>/', views.solve),
 		path('remove/<int:item_id>/', views.remove),
 		path('save/', views.save),
]
