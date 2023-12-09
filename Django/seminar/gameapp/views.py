from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from random import randint, choice
import logging
from .models import Headtails


logger = logging.getLogger(__name__)


def index(request):
    context = {'name': 'olga'}
    logger.info('Index page accessed')
    return render(request, "gameapp/index.html", context)


def about(request):
    my_list = ['apple', 'banana', 'orange']
    name = 'olga'
    context = {'my_list': my_list, 'name': name}
    logger.info('About page accessed')
    return render(request, "gameapp/about.html", context)


def rolls(request, roll):
    h_t = []
    cbs = []
    hnd = []
    for i in range(roll):
        h_t.append(choice(["Head","Tail"]))
        cbs.append(randint(1,6))
        hnd.append(randint(0,100))
    context = {'roll': roll, 'h_t': h_t, 'cbs': cbs, 'hnd': hnd}
    return render(request, 'gameapp/game_result.html', context)


def head_tails(request):
    side = choice(["Head","Tail"])
    coin = Headtails(result=side)
    coin.save()
    return HttpResponse(f'Поздравляю! у вас {side}')


def game_roll(request, roll):
    path = str(request).split('/')[2]
    if path == 'headtails':
        name = 'орел и решка'
        game_lst = []
        for i in range(roll):
            game_lst.append(choice(["Head","Tail"]))
    elif path == 'cubes':
        name = 'кости'
        game_lst = []
        for i in range(roll):
            game_lst.append(randint(1,6))
    else:
        name = 'сотня'
        game_lst = []
        for i in range(roll):
            game_lst.append(randint(0,100))
    context = {'roll': roll, 'game_lst': game_lst, 'name': name}
    return render(request, 'gameapp/game.html', context)


def headtails_values(request):
    value = Headtails.values()
    lst = list(i.result for i in value)
    count_h = 0
    count_t = 0
    for i in lst:
        if i == 'Head':
            count_h += 1
        else: count_t += 1
    return HttpResponse(f'Статистика последних пяти бросков "Head"  выпало {count_h} раз, "Tail" -  {count_t} ')


def cubes(request):
    return HttpResponse(f'{randint(1,6)}')


def hundred(request):
    return HttpResponse(f'{randint(0,100)}')
