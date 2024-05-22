# django model setting
from django.db import models
from django.contrib.auth import get_user_model

from django.conf import settings

User = get_user_model()

class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    content = models.TextField('내용')
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    view_count = models.IntegerField('조회수', default=0)
    writer = models.ForeignKey( #1대 다일때 이용하는 함수. 한 게시글을 여러 작성자가 쓸 수 없게 방지함
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE) #같은 코멘트가 여러 포스트에 달릴 수 없도록 방지
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
#settings.AUTH_USER_MODEL : 장고가 저장해둔 기본으로 지원하는 모델을 가리키는 함수
#이거를 accounts 폴더에 있는 models.py에 등록된 User를 가리키도록 바꿔줘야 함
# DB가 좀 망한 것 같다 하면 그냥 posts 폴더 - migrations - 0001_initial.py 삭제, db.sqlite3 삭제하고
# migrations 다시 하기
