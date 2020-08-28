# from django.urls import path, include, re_path # 정규표현식 사용하기 위해서
# from blog import views

# app_name = 'blog' # namespace 지정해야 한다.

# urlpatterns = [
#     path('', views.PostLV.as_view(), name='index'), # /blog/로 요청했을 때

#     # Example : /blog/post/ (/blog/와 동일한 응답)
#     # name만 post_list로 하면 된다.
#     path('post/', views.PostLV.as_view(), name='post_list'),

#     # Example : /blog/post/slug텍스트/
#     # PostDV : views.py 에 추가
#     # slug에 허용되는 문자열 형태, postDV가 이 요청 처리, as_view()로 동작한다.
#     re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'), 

# ]

from django.urls import path, re_path
from blog import views

app_name='blog'
urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),    
    
    # Example: /blog/post/ (same as /blog/)
    path('post/', views.PostLV.as_view(), name='post_list'),

    # Example: /blog/post/slug텍스트/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    # Example : /blog/search/
    path('search/', views.SearchFormView.as_view(), name='search')
]
