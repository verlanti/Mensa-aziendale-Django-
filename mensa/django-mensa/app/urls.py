# app/urls.py
from django.urls import path, include
from . import views


app_name = 'app'

urlpatterns = [

        path('menu/', views.Menu.as_view(), name='menu'),
        path('changemenu/', views.changeMenu, name='changemenu'),
        path('menu/<int:id>/deletemenu', views.deleteMenu, name='deletemenu'),

        path('insertplate/', views.insertPlate, name='insertplate'),
        #path('insertplate/', views.InsertPlate.as_view(), name='insertplate'),
        path('listplate/', views.ListPlates.as_view(), name = 'listplate'),
        path('listplate/<int:id>/changeplate', views.changePlate, name='changeplate'),
        path('listplate/<int:id>/deleteplate', views.deletePlate, name='deleteplate'),
        path('listordini/',views.ListOrdini.as_view(), name='listordini'),

        path('ordine/',views.ordine,name='ordine'),
        path('ordine/<int:id>/deleteordine', views.deleteOrdine, name='deleteordine'),
        

        path('statistics/',views.StatisticsList.as_view(), name='statistics'),


]
