from django.db import models

# Create your models here.
class HH(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    number = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    Sdate = models.CharField(max_length=255, default="")#startdate
    Edate = models.CharField(max_length=255, default="")#enddate
    eg_name = models.CharField(max_length=255, default="")#英文品名
    ch_name = models.CharField(max_length=255, default="")#中文品名
    Element = models.CharField(max_length=255, default="")#成分
    dose = models.CharField(max_length=255, default="")#劑量
    company_name = models.CharField(max_length=255, default="")#公司名稱
    
class HH2(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    number = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    Sdate = models.CharField(max_length=255, default="")#startdate
    Edate = models.CharField(max_length=255, default="")#enddate
    eg_name = models.CharField(max_length=255, default="")#英文品名
    ch_name = models.CharField(max_length=255, default="")#中文品名
    Element = models.CharField(max_length=255, default="")#成分
    dose = models.CharField(max_length=255, default="")#劑量
    company_name = models.CharField(max_length=255, default="")#公司名稱
    
