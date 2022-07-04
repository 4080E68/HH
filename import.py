from linebotApp.models import HH
import django
import csv
import sys
import os

project_dir = "/Users/user/0704/linebot_project/linebot_project"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'linebot_project.settings'
django.setup()
data = csv.reader(
    open("/Users/user/0704/linebot_project/0704.csv"), delimiter=",")
for row in data:
    unit = HH()
    unit.number = row[0]
    unit.price = row[1]
    unit.text = row[2]
    unit.save()
