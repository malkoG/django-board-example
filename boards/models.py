from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name="제목")
    content = models.TextField(verbose_name="게시판 내용")
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        db_table = 'boards'
        verbose_name = '게시판'
        verbose_name_plural = '게시판 목록'

    def __str__(self):
        return self.title