from django.db import models

# Create your models here.
class HH(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    number = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    text = models.CharField(max_length=255, default="")
    
