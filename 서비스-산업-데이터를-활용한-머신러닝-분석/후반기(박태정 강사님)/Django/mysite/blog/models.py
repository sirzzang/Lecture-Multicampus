from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="TITLE", max_length=50)
    # 제목 : 문자, 최대 길이 50 + verbose_name(로그 정보에 나올 이름) 지정 가능.
    slug = models.SlugField('SLUG', 
                            unique=True, allow_unicode=True, 
                            help_text = '제목 별칭으로 한 단어를 입력하세요.')
    # 슬러그 : 글 내용 요약. 해시태그와 비슷한 역할. model의 slugfield. 유니코드, 힌트 텍스트 지정.
    description = models.CharField(verbose_name="DESCRIPTION", max_length=100,
                                    blank=True, help_text="작성할 내용을 입력하세요.")
    content = models.TextField('CONTENT') # 글 내용: 길이 제한 없음.
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True) # 작성 일자 자동
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

    class Meta: # 내부 클래스 : 메타 정보 저장
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts' # sqlite3 DB의 테이블과 연동.
        ordering = ('-modify_dt', ) # 최신 수정된 날짜, 내림차순.
    
    def __str__(self): # 제목 반환
        return self.title
    
    def get_absolute_url(self): # 절대주소 반환
        return reverse('blog:post_detail', args=(self.slug, ))
    
    def get_previous(self): # 이전 페이지 반환
        return self.get_previous_by_modify_dt()
    
    def get_next(self): # 다음 페이지 반환
        return self.get_next_by_modify_dt()





