from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
def display(request):
    return HttpResponse('IAM VINAY ,IAM VERY COOL')


from .models import databases
obj=databases(student_id=1,first_name="Alice",last_name="Smith",age=18,
grade=95.5)
obj.save()
databases.objects.filter(first_name="Alice").update(grade=97.0)

databases.objects.filter(last_name="Smith").delete()

all_files_databases=databases.objects.all()
for items in all_files_databases:
    print(items.student_id,items.first_name,items.last_name,items.age,
    items.grade)       

