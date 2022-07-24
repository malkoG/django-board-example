from django.urls import path

from boards.views import BoardListCreateAPIView

urlpatterns = [
    path('', BoardListCreateAPIView.as_view(), name="board_list")
]