# coding:utf-8
from game.models import Goods, Character

class initialize(object):
    def game_goods(self):
        # g = Goods(name='茅台酒', category='1', type='1')
        goods = [
                # {'name':'茅台酒', 'category':'1', 'type':'1'},
                # {'name':'美国大豆', 'category':'6', 'type':'1'},
                # {'name':'螺纹钢', 'category':'5', 'type':'1'},
                # {'name':'苹果手机', 'category':'2', 'type':'1'},
                # {'name':'北京地产', 'category':'3', 'type':'1'},
                # {'name':'中华香烟', 'category':'1', 'type':'1'},
                # {'name':'奔驰汽车', 'category':'4', 'type':'1'},
                # {'name':'智利铜矿', 'category':'7', 'type':'1'},
             ]
        for good in goods:
            g = Goods(name=good['name'], category=good['category'], type=good['type'])
            g.save()

    def game_character(self):
        # c = Character(name='孔雀', risk=50, health=30, energy=100, happiness=40, wisdom=40)
        characters = [
            # {'name':'狮子', 'risk':70, 'health':30, 'energy':100, 'happiness':40, 'wisdom':40},
            # {'name':'孔雀', 'risk':50, 'health':30, 'energy':100, 'happiness':40, 'wisdom':40},
            # {'name':'兔子', 'risk':70, 'health':30, 'energy':100, 'happiness':40, 'wisdom':40},
            # {'name':'变色龙', 'risk':70, 'health':30, 'energy':100, 'happiness':40, 'wisdom':40},
        ]
        for character in characters:
            c = Character(name = character['name'], risk=character['risk'], health=character['health'],
                          energy=character['energy'], happiness=character['happiness'], wisdom=character['wisdom'])
            c.save()
