from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from drf_yasg.utils import swagger_auto_schema

from boards.serializers import BoardSerializer
from boards.models import Board
from . import schemas


class BoardListCreateAPIView(ListCreateAPIView):
      queryset = Board.objects.all()
      serializer_class = BoardSerializer

      @swagger_auto_schema(**schemas.board_list_schema)
      def get(self, *args, **kwargs):
            return super().get(*args, **kwargs)

      @swagger_auto_schema(**schemas.board_create_schema)
      def post(self, *args, **kwargs):
            return super().post(*args, **kwargs)

