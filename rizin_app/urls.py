from django.urls import path
from . import views

app_name = 'rizin_app'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('player_list/', views.player_list, name='player_list'),
    path('bantamrank_create/', views.BantamrankCreateView.as_view(), name='bantamrank_create'),
    path('featherrank_create/', views.FeatherrankCreateView.as_view(), name='featherrank_create'),
    path('bantamrank_list/', views.BantamrankListView.as_view(), name='bantamrank_list'),
    path('featherrank_list/', views.FeatherrankListView.as_view(), name='featherrank_list'),

]