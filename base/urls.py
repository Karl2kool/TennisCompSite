from django.urls import path
from .views import ManageReserve, ManageScore, Management,MatchCreate, ReserveList,MatchUpdate, ReserveUpdate, ScoreBoard, Home, CustomLoginView, Management,ManageMatches,ReserveCreate, ScoreCreate, ReserveDelete, ScoreUpdate,Week,MatchesByWeekView
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),
    path('management', Management.as_view(), name='manager'),
    
    path('', Home.as_view(), name='home'),
    path('reserves/',ReserveList.as_view(), name='reserve'),
    path('scoreboard/',ScoreBoard.as_view(), name='score'),
   
    path('matches/', MatchesByWeekView.as_view(), name='matches_by_week'),


    path('management/reserve',ManageReserve.as_view(), name='managereserve'),
    path('management/reserve/create', ReserveCreate.as_view(), name='reserve-create'),
    path('management/reserve/edit/<int:pk>/',ReserveUpdate.as_view(), name='reserve-update'),
    path('management/reserve/delete/<int:pk>/', ReserveDelete.as_view(), name='reserve-delete'),

    path('management/score/', ManageScore.as_view(), name='managescore'),
    path('management/score/edit/<int:pk>',ScoreUpdate.as_view(), name='scoreupdate'),
    path('management/score/create/', ScoreCreate.as_view(), name='score-create'),

    path('management/match/', ManageMatches.as_view(), name='managematch'),
    path('management/match/edit/<int:pk>/', MatchUpdate.as_view(), name='matchupdate'),
    path('management/match/create/', MatchCreate.as_view(), name='matchcreate'),

    


]