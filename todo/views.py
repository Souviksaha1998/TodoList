from django.shortcuts import render , HttpResponse , redirect
from todo.models import Todo
from django.http import Http404
from django.contrib import messages


# Create your views here.
def index(request):
   task = Todo.objects.all()
   context = {'task' : task}
   if request.POST.get('todos')=="":
      messages.error(request,"Please , Add todo.....")
      return  render(request , 'index.html' , context);
   else:
      if request.method =='POST': 
         t1 = request.POST.get('todos')
         t1 = Todo(new_task = t1)
         t1.save()
         messages.success(request, 'Todo Added')
   return  render(request , 'index.html' , context);

def delete(request, todo_id):
   try:
      todoss = Todo.objects.get(id=todo_id)
      todoss.delete()
      messages.warning(request, 'Todo deleted')
      return redirect('index')
   except:
      return HttpResponse('error')


   
  