from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=64)
    category = models.IntegerField(verbose_name='1-零售 2-科技 3-不动产 4-运输 5-制造业 6-农林牧渔 7-资源')
    type = models.SmallIntegerField(verbose_name='类型 1-实物 2-股票 3-虚拟物品',)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_good_type(self):
        return self.type

class Character(models.Model):
    name = models.CharField(max_length=63)
    risk = models.SmallIntegerField(verbose_name='风险偏好')
    health = models.SmallIntegerField(verbose_name='健康度')
    energy = models.SmallIntegerField(verbose_name='精力值')
    happiness = models.SmallIntegerField(verbose_name='快乐度')
    wisdom = models.SmallIntegerField(verbose_name='智力')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Relationship(models.Model):
    name = models.CharField(max_length=63)
    default = models.SmallIntegerField(verbose_name='默认关系值')
    code = models.SmallIntegerField(verbose_name='code值')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Game_Goods(models.Model):
    good_id = models.IntegerField()
    good_name = models.CharField(max_length=64)
    status = models.SmallIntegerField(verbose_name='状态 0-市场 ',default=0)
    type = models.SmallIntegerField(verbose_name='类型 0-实物 1-股票 2-虚拟物品',)
    stock = models.IntegerField(verbose_name='库存量')
    owner_id = models.IntegerField(verbose_name='拥有者 0-匿名市场货物  ')
    isOnsale = models.SmallIntegerField(verbose_name='是否在售', default=0)
    producer = models.IntegerField(verbose_name='生产厂商', default=0)
    period = models.IntegerField(verbose_name='保质期天数')
    created = models.DateTimeField(auto_now_add=True, verbose_name='生产日期')
    quality = models.IntegerField(verbose_name='产品质量')
    game_id = models.IntegerField(verbose_name='游戏局id')
    round_id = models.IntegerField(verbose_name='回合id')

    def __str__(self):
        return self.good_name

class Game_Price(models.Model):
    good_id = models.IntegerField(verbose_name='商品id')
    price = models.DecimalField(verbose_name='当前售价',decimal_places=2, max_digits=11)
    game_id =models.IntegerField(verbose_name='游戏局id')
    round_id = models.IntegerField(verbose_name='回合id')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.price

class Game_Market(models.Model):
    good_id = models.IntegerField(verbose_name='商品id')
    good_name = models.CharField(max_length=64)
    demands = models.IntegerField(verbose_name='需求量')
    produce = models.IntegerField(verbose_name='生产量')
    game_id =models.IntegerField(verbose_name='游戏局id')
    round_id = models.IntegerField(verbose_name='回合id')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.good_name

class Game_Orders(models.Model):
    seller_id = models.IntegerField(verbose_name='卖家id')
    buyer_id = models.IntegerField(verbose_name='买家id')
    good_id = models.IntegerField(verbose_name='商品id')
    good_name = models.CharField(max_length=64)
    price = models.DecimalField(verbose_name='成交价',decimal_places=2, max_digits=11)
    game_id =models.IntegerField(verbose_name='游戏局id')
    round_id = models.IntegerField(verbose_name='回合id')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.good_name

class Game_Player(models.Model):
    name = models.CharField(max_length=63)
    character_id = models.SmallIntegerField(verbose_name='人物id')
    health = models.SmallIntegerField(verbose_name='健康度')
    energy = models.SmallIntegerField(verbose_name='精力值')
    happiness = models.SmallIntegerField(verbose_name='快乐度')
    cash = models.DecimalField(verbose_name='现金',decimal_places=2, max_digits=14)
    game_id =models.IntegerField(verbose_name='游戏局id')
    round_id = models.IntegerField(verbose_name='回合id')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Game_Relationship(models.Model):
    player_id = models.IntegerField(verbose_name='人物id')
    player_name = models.CharField(max_length=64)
    objecter_id = models.IntegerField(verbose_name='对方id')
    objecter_name = models.CharField(max_length=64)
    relation_code = models.IntegerField(verbose_name='0-陌生人 11-恋人  12-夫妻   21-父  22-母 31-子 32-女 41-兄 42-弟 43-姐 44-妹  51-同学  61-同事  71-聚会  81-酒吧 91-旅游' )
    game_id =models.IntegerField(verbose_name='游戏局id')
    round_id = models.IntegerField(verbose_name='回合id')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.player_id

    def get_objector_name(self):
        return self.objecter_name