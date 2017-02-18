from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from web.models import User, Token, Expense, Income

from django.views.decorators.csrf import csrf_exempt

from datetime import datetime

# Create your views here.

@csrf_exempt
def submit_income(request):
    """user submits and expense """

    #TODO valid might be fake

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' in request.POST:
        date = request.POST['date']
    else:
        date = datetime.now()
    Income.objects.create(user=this_user, amount=request.POST['amount'], text = request.POST['text'], date=date)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_expense(request):
    """user submits and expense """

    #TODO valid might be fake

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' in request.POST:
        date = request.POST['date']
    else:
        date = datetime.now()
    Expense.objects.create(user=this_user, amount=request.POST['amount'], text = request.POST['text'], date=date)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)
