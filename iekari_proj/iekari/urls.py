# path()関数のインボート 
from django.urls import path
from . import views 
# ルーティングの設定 

urlpatterns = [ 
    path('hello/', views.hello, name='hello'), 
]