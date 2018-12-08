from django.http import HttpResponse
from .models import *


def hello(request):
    return HttpResponse('Hello!!!')


def get_persons(request) -> HttpResponse:
    person = ['%s' % person.name for person in Person.objects.all()]
    return HttpResponse('<p>'.join(person))


def get_person(request, first_name, last_name, parameter) -> HttpResponse:
    if last_name is not None:
        name = first_name + last_name
    else:
        name = first_name

    if parameter is None:
        person = ['<b>Age:</b> %s; <b>profession:</b> %s' % (person.age, person.profession) for person in Person.objects.all() if person.name == name]
    else:
        if parameter == 'age':
            person = ['<b>Age:</b> %s' % person.age for person in Person.objects.all() if person.name == name]
        elif parameter == 'profession':
            person = ['<b>Profession:</b> %s' % person.profession for person in Person.objects.all() if person.name == name]

    if not person:
        return HttpResponse('Person is not found')
    return HttpResponse('<p>'.join(person))
