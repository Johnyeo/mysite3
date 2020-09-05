from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from game import db_init
from game.models import Character


def index (request):
    return render(request, 'game/index.html')

def profile(request, character_id):
    c = Character.objects.get(id=character_id)
    print(c)
    print(c.name)
    c2 = Character.objects.extra(select={'greater_than_30':"wisdom>10"})
    c3 = Character.objects.extra(where=["wisdom > 10"])
    print(c3[1].name)

    return HttpResponse( 'NO.%sThis is the profile /n name: %s and %s' %(character_id, c.name, c3[0].name))

def initializeDatabase(request, db_id):
    db_id = int(db_id)
    if db_id == 1:
        db_init.initialize().game_goods()
        res = 'game_goods'
    elif db_id == 2:
        db_init.initialize().game_character()
        res = 'game_character'

    return HttpResponse('%s init finished' % res)
