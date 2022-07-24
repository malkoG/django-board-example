from rest_framework import status
from drf_yasg.openapi import Parameter, Response
from drf_yasg import openapi

from boards.serializers import BoardSerializer


class BoardResponse(BoardSerializer):
    pass


board_list_schema = {
    "tags": ["게시판"],
    "operation_id": "board_list",
    "operation_summary": "게시글의 리스트",
    "operation_description": """
    게시글의 리스트를 반환하는 API입니다.
    """,
    "responses": { status.HTTP_200_OK: Response("", BoardResponse(many=True)) }
}

board_create_schema = {
    "tags": ["게시판"],
    "operation_id": "board_create",
    "operation_summary": "게시글 생성",
    "operation_description": """
    게시글을 생성하는 API입니다.
    """,
    "responses": { status.HTTP_200_OK: Response("", BoardResponse()) }
}