from django.db import models

# Create your models here.

class Todo(models.Model):
    content = models.CharField(max_length = 255) # 문자열 속성 필드 컬럼 생성
    # model의 property 생성 가능 : charfield, textfield, filepathfield 등
    isDone = models.BooleanField(default=False) # 기본값은 False. 수정되면 True로 바뀜.
