from django.conf import settings
from linebotApp.models import *

from linebot import LineBotApi
from linebot.models import DatetimePickerTemplateAction, LocationSendMessage, MessageAction, QuickReplyButton, QuickReply, StickerSendMessage, TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn, ImageSendMessage
import datetime
import requests
import pygsheets
import pandas as pd
import gspread
from urllib.request import urlretrieve
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def manageForm(event, mtext):  # liff表單

    flist = mtext[3:].split('&')
    number = flist[0].upper()  # 健保碼
    ch_name = flist[1]
    eg_name = flist[2].upper()
    Element = flist[3].upper()
    gc = pygsheets.authorize(
        service_file='/Users/user/0704/linebot_project/linebotApp/toad-slby-b1f755b2fa87.json')
    sht = gc.open_by_url(
        'https://docs.google.com/spreadsheets/d/1QaKwk9dVFBRxrKIHUorJ4JjbO4iIfh1MpI-pacDcQLE/edit?usp=sharing'
    )
    wks_list = sht.worksheets()  # 確認連結
    print(wks_list)
    wks = sht[0]  # 選擇工作表
    print(wks)
    # 讀取成 df
    df = pd.DataFrame(wks.get_all_records())
    # 讀取 df 也可以這樣寫
    wks.get_as_df()
    filt = df['number'].str.contains(number) & df['ch_name'].str.contains(ch_name) &\
        df['eg_name'].str.contains(
            eg_name) & df['element'].str.contains(Element)  # 篩選條件
    result = df.loc[filt]  # 執行
    print("查詢結果為%s筆資料" % len(result))
    i = 0
    final = ''
    while (i < len(result)):
        final += "健保碼：" + str(result.iloc[i]['number']) + "\n" + "價格：" + \
            str(result.iloc[i]['price']) + "\n" + "成分：" + str(result.iloc[i]['element']) + "\n" + \
            "中文名稱：" + str(result.iloc[i]['ch_name']) + "\n" + \
            "英文名稱：" + str(result.iloc[i]['eg_name']) + "\n\n"
        i += 1
    print("共有%s筆資料" % i)
    if(len(final) >= 2000):
        final = "資料筆數過多！"
    elif(len(final) <= 0):
        final = "查無資料！"

    reply_arr = []

    reply_arr.append(TextSendMessage(text="查詢結果為：" + str(len(result))))
    reply_arr.append(TextSendMessage(text=final))
    # print(reply_arr)
    line_bot_api.reply_message(event.reply_token, reply_arr)
