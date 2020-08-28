from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView # 상속받아야 하므로, import
from blog.models import Post # post class 사용
from django.db.models import Q
from blog.forms import PostSearchForm

# ListView 상속받는다.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html' # 처음에 요청할 때 볼 수 있는 페이지
    context_object_name = 'posts'
    paginate_by = 2

#--- DetailView : 장고 프레임워크에서 제공하는 class를 상속받아서 진행하면 된다.
class PostDV(DetailView):
    model = Post

#--- FormView : 검색 기능 구현 위해 FormView 상속받는다.
class SearchFormView(FormView):
    form_class = PostSearchForm # object 정의해야 한다 : 
    template_name = 'blog/post_search.html' # post_search html 양식에서 검색어 입력하면 검색어가 넘어올 것.

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word'] # 앞뒤 공백 제거, 파라미터 : search_word(폼 클래스에 search_word라고 지정한 변수)

        post_list = Post.objects.filter( Q(title__icontains=searchWord)| Q(description__icontains=searchWord)| Q(content__icontains=searchWord)).distinct
        # Q함수 이용해 searchword 포함되어 있는지 체크 : title, description, content
        # 똑같은 검색어가 있을 때 중복으로 가져오지 않도록 SQL distinct로 중복 제거.

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

