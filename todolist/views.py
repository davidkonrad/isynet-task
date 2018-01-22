from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers
from datetime import datetime
from .models import TodoItem

#main
def index(request):
    template = loader.get_template('todolist/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

#get all todo items
def tasks(request):
    todoitem_list = TodoItem.objects.all().order_by('-created_timestamp')
    template = loader.get_template('todolist/tasks.html')
    context = {
        'todoitem_list': todoitem_list
    }
    return HttpResponse(template.render(context, request))

#get a single todo item by id
def item(request, item_id):
    todoitem = get_object_or_404(TodoItem, id=item_id)
    json = serializers.serialize("json", [todoitem])
    return HttpResponse(json, content_type="application/json")

#mark a todo item as solved
def solve(request, item_id):
    todoitem = get_object_or_404(TodoItem, id=item_id)
    todoitem.solved_timestamp = datetime.now()
    todoitem.save()
    json = serializers.serialize("json", [todoitem])
    return HttpResponse(json, content_type="application/json")

#remove a todo item
def remove(request, item_id):
    todoitem = get_object_or_404(TodoItem, id=item_id)
    todoitem.delete()
    return JsonResponse( { 'success': 'Todo item removed' } )

#update or create a todo item
def save(request):
    if request.GET['id']:
        todoitem = TodoItem.objects.get(id=request.GET['id']);
        todoitem.title = request.GET['title']
        todoitem.description = request.GET['description']
        todoitem.save()
        return JsonResponse( { 'success': 'Todo item updated' } )
    else:
        todoitem = TodoItem(title=request.GET['title'], description=request.GET['description']) 
        todoitem.save()       
        return JsonResponse( { 'success': 'New todo item created' } )



