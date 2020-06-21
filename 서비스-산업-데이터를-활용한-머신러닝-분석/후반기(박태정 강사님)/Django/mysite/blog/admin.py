from django.contrib import admin
from blog.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): # admin의 ModelAdmin 상속받음.
    list_display = ('id', 'title', 'modify_dt',) # 기본적으로 보여지는 필드
    list_filter = ('modify_dt',) # 필터링 필드

    search_fields = ('title', 'content',) # 제목, 내용으로 검색
    prepopulated_fields = {'slug':('title', )}  # 슬러그 필드
