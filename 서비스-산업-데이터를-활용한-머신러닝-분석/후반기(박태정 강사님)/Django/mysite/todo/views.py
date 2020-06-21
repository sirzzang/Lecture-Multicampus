from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse


# Create your views here.

# 1. index 구성
def index(request) :
    # return HttpResponse("todo app first page") # 초기 페이지 생성 확인용 텍스트
    todo_list = Todo.objects.all() # todo 객체에서 DB object를 가져온다.
    content = {'todos':todo_list} # dictionary로 만든다.
    return render(request, 'todo/index.html', content) # content 넘긴다.

# 2. createTodo 구성
def createTodo(request):
    # return HttpResponse("todo app ... createTodo ok?") # 테스트용
    user_input = request.POST['todoContent'] # input box의 id/name이 todoContent이고, 여기에 post요청.
    todo_obj = Todo(content=user_input)
    todo_obj.save()
    # return render(request, 'todo/index.html')
    return HttpResponseRedirect(reverse('index'))

# 3. doneTodo 구성
def doneTodo(request):
    done_id = request.GET['todoNum'] # 글번호 : todoNum을 파라미터로 넘겨준다.
    print("완료된 todo의 id :", done_id) # 확인을 위한 출력
    todo = Todo.objects.get(id=done_id) # 완료된 id를 이용해 todo 객체 생성
    todo.isDone = True # 작업 끝났을 때 True로 변경
    todo.save()
    return HttpResponseRedirect(reverse('index')) # 'index'로 다시 돌아가서 redirect

