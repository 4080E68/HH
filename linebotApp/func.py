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
    # number_like = '%'+number+'%'
    # number_like2 = number+'%'
    ch_name = flist[1]
    eg_name = flist[2]
    Element = flist[3].upper()
    # ch_like = '%'+flist[1]+'%'
    # ch_like2 = flist[1]+'%'
    # ch_like3 = '%'+flist[1]
    # eg_like = '%'+flist[2]+'%'
    # eg_like2 = flist[2]+'%'
    # eg_like3 = '%'+flist[2]
    # Element_like = '%'+flist[3]+'%'
    # Element_like2 = flist[3]+'%'
    # Element_like3 = '%'+flist[3]
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
    # print(df)
    #filt = (df['number'] == 'A001584100') & (df['id'] == 1)#
    filt = df['number'].str.contains(number) & df['ch_name'].str.contains(ch_name) &\
    df['eg_name'].str.contains(eg_name) & df['Element'].str.contains(Element) # 篩選條件
    result = df.loc[filt]
    # print(len(result))
    i = 0
    while (i < len(result)):
        print("第%s筆資料" % i)
        print(result.iloc[i]['id'])
        print(result.iloc[i]['number'])
        print(result.iloc[i]['ch_name'])
        print(result.iloc[i]['eg_name'])
        print(result.iloc[i]['Sdate'])
        print(result.iloc[i]['Edate'])
        i += 1
    # result = HH2.objects.raw(
    #     'SELECT * FROM linebotApp_HH2 where number LIKE %s  and (ch_name LIKE %s or ch_name LIKE %s or ch_name LIKE %s ) and (eg_name LIKE %s or eg_name LIKE %s or eg_name LIKE %s) and (Element LIKE %s or Element LIKE %s or Element LIKE %s)',
    #     [number_like,  ch_like, ch_like2, ch_like3, eg_like, eg_like2, eg_like3, Element_like, Element_like2, Element_like3])
    # print(result.query)
    # final = ''
    # print("查詢數量為：" + str(len(result)))

    # for i in result:
    #     final += "健保碼：" + str(i.number) + "\n" + "價格：" + \
    #         str(i.price) + "\n" + "成分：" + str(i.Element) + "\n" + \
    #         "中文名稱：" + str(i.ch_name) + "\n" + \
    #         "英文名稱：" + str(i.eg_name) + "\n\n"
    # if(len(final) >= 2000):
    #     final = "資料筆數過多！"
    # elif(len(final) <= 0):
    #     final = "查無資料！"

    reply_arr = []

    reply_arr.append(TextSendMessage(text="查詢結果為：" + str(len(result))))
    reply_arr.append(TextSendMessage(text=final))

    print(reply_arr)
    line_bot_api.reply_message(event.reply_token, reply_arr)
