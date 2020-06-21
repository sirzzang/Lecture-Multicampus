from django.urls import path
from . import views # 현재 디렉토리 아래에서 views 가져옴.

# url의 '' 요청에 대해서 view.py에 정의된 index 함수 호출. 해당 과정을 mapping.
urlpatterns = [
    path('', views.index, name="index"),
    # view : 컨트롤러 정의하는 views.py 함수. -> 여기서 index 호출함.
    path('createTodo', views.createTodo, name="createTodo"),
    # createTodo url로 접근했을 때, views.py 에서 createTodo 함수 호출.
    path('doneTodo', views.doneTodo, name="doneTodo"), # 완료했을 때
    
]