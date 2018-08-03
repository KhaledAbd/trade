app_name = 'Triko'

from django.urls import path
from .views import  show_details,get_Model,Like,change_pic,listing

urlpatterns = [
    path('', listing, name= 'triko_model'),
    path('model/<int:id>/', show_details, name='show_details'),
    path('model/<int:id>/demind/', get_Model, name = 'get_models'),
    path('like/<int:id>/', Like, name = 'like'),
    path('model/<int:id>/image', change_pic, name='change_pic'),

]