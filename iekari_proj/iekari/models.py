from django.contrib.auth.models import User 
from django.db import models 
 
GENDER_LIST = ( (0, '男性'), (1, '女性') )
dict_gender_list = {0:'男性',1:'女性'}

#デフォルトであるdjango.dbのmodelsを継承して作成する
class Profile(models.Model):
    
    #django仕様のメタクラス(クラス自体の設定を記述)(管理画面での表示内容を設定)
    class Meta:
        verbose_name = 'ユーザー情報データ'
        verbose_name_plural = 'ユーザー情報データ'
    #ユーザーの設定。下記のフィールドとの紐づけはビューで行う
    user = models.OneToOneField(User, verbose_name='ユーザー',null=True, blank=True, on_delete=models.CASCADE)

    #フィールドの設定。コード１行がフィールド１列に対応する。
    id = models.CharField(max_length=6,primary_key=True)
    age = models.IntegerField('年齢')
    gender = models.IntegerField('性別',choices=GENDER_LIST)
    household_num = models.IntegerField('世帯人数')
    
    #管理画面で表示される文字列を定義する
    def __str__(self):
        return self.id+' '+str(self.age)+'歳 ' \
            +dict_gender_list.get(self.gender)+' ' \
            +str(self.household_num)+'人世帯 ' 

# class RentRoom(models.Model):
    
    #django仕様のメタクラス(クラス自体の設定を記述)(管理画面での表示内容を設定)
    # class Meta:
    #     verbose_name = 'お家データ'
    #     verbose_name_plural = 'お家データ'
    # #ユーザーの設定。下記のフィールドとの紐づけはビューで行う
    # user = models.ForeignKey(User, verbose_name='お家',null=True, blank=True, on_delete=models.CASCADE)

    # #フィールドの設定。コード１行がフィールド１列に対応する。
    # id = models.CharField(max_length=6,primary_key=True)
    # pref_name = models.CharField('都道府県名', max_length=6,primary_key=True)
    # city_name = models.CharField('市名', max_length=6,primary_key=True)
    # district_name = models.CharField('区町村名',max_length=6,primary_key=True)
    # built_year = models.IntegerField('築年数')
    # structure = models.CharField('構造',max_length=6,primary_key=True)
    # top_floor_num = models.IntegerField('最上階')
    # room_type = models.CharField('間取り',max_length=6,primary_key=True)
    # price = models.FloatField('価格')
    # area = models.FloatField('エリア')
    # latitude = models.FloatField('緯度')
    # longiitude = models.FloatField('経度')
    # nearest_station = models.CharField('最寄り駅', max_length=6,primary_key=True)
    # dist_to_nearest_station = models.FloatField('最寄り駅からの距離')
    #管理画面で表示される文字列を定義する

class RentRoom(models.Model):
    class Meta:
        verbose_name = '賃貸物件データ'
        verbose_name_plural = '賃貸物件データ'
    
    id = models.CharField('物件ID',max_length=6,primary_key=True) # 'A00001'
    pref_name = models.CharField('都道府県',max_length=20)      # '東京都'
    city_name = models.CharField('市区町村',max_length=50)      # '世田谷区'
    district_name = models.CharField('町丁目',max_length=50)    # '喜多見７丁目'
    built_year = models.IntegerField('築年')
    structure = models.CharField('構造',max_length=20)
    top_floor_num = models.IntegerField('最上階数')
    room_type = models.CharField('間取り',max_length=20)        # '1R', '1K' など
    price = models.FloatField('平米単価')
    area = models.FloatField('専有面積')
    latitude = models.FloatField('物件緯度')
    longitude = models.FloatField('物件経度')
    nearest_station = models.CharField('最寄り駅', max_length=50)
    dist_to_nearest_station = models.FloatField('最寄駅までの距離')

    def __str__(self):
        return self.id

    # def __str__(self):
    #     return self.id+' '+self.pref_name+'県 ' \
    #         +self.city_name+'市 ' \
    #         +self.district_name+'町 ' \
    #         +'築 '+ str(self.built_year)+'年 ' \
    #         +self.structure \
    #         +'最上階 '+ str(self.top_floor_num)+'階 ' \
    #         +'ルームタイプ '+ self.room_type \
    #         +'価格 '+ str(self.price) \
    #         +'エリア '+ str(self.area) \
    #         +'緯度 '+ str(self.latitude) \
    #         +'経度 '+ str(self.longiitude) \
    #         +'最寄り駅 '+ self.nearest_station+'駅 ' \
    #         +'駅から '+ str(self.dist_to_nearest_station)+'m ' \

    # def __str__(self):
    #     return self.id+' '+str(self.pref_name)+'県 ' \
    #         +str(self.city_name)+'市 ' \
    #         +str(self.district_name)+'町 ' \
    #         +'築 'str(self.built_year)+'年 ' \
    #         +str(self.structure) \
    #         +'最上階 '+ str(self.top_floor_num)+'階 ' \
    #         +'ルームタイプ '+ str(self.room_type) \
    #         +'価格 '+ str(self.price) \
    #         +'エリア '+ str(self.area) \
    #         +'緯度 '+ str(self.latitude) \
    #         +'経度 '+ str(self.longiitude) \
    #         +'最寄り駅 '+ str(self.nearest_station)+'駅 ' \
    #         +'駅から '+ str(self.dist_to_nearest_station)+'m '