from django.conf import settings
from linebotApp.models import *

from linebot import LineBotApi
from linebot.models import DatetimePickerTemplateAction, LocationSendMessage, MessageAction, QuickReplyButton, QuickReply, StickerSendMessage, TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn, ImageSendMessage
import datetime
import requests
from urllib.request import urlretrieve
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


# def healthy(event, mtext):
#     text = mtext[3:]
#     text = text.upper()
#     seconds = time.time()
#     local_time = time.ctime(seconds)
#     print("現在時間:"+local_time + '\n' + "輸入文字:" + text)
#     if health.objects.filter(number=text).exists():
#         Hdata = health.objects.filter(number__iexact=text)[0]
#         message = "健保價格為:" + str(Hdata.price)
#     elif health.objects.filter(text=text).exists():
#         Hdata = health.objects.filter(text__iexact=text)[0]
#         message = "健保價格為:" + str(Hdata.price)
#     else:
#         message = "查無資料!!"

#     line_bot_api.reply_message(
#         event.reply_token, TextSendMessage(text=str(message)))


def manageForm(event, mtext):  # liff表單

    flist = mtext[3:].split('&')
    number = flist[0].upper()  # 健保碼
    number_like = '%'+number+'%'
    number_like2 = number+'%'
    ch_name = flist[1]
    eg_name = flist[2]
    Element = flist[3].upper()
    ch_like = '%'+flist[1]+'%'
    ch_like2 = flist[1]+'%'
    ch_like3 = '%'+flist[1]
    eg_like = '%'+flist[2]+'%'
    eg_like2 = flist[2]+'%'
    eg_like3 = '%'+flist[2]
    Element_like = '%'+flist[3]+'%'
    Element_like2 = flist[3]+'%'
    Element_like3 = '%'+flist[3]
    # if(ch_name == '' and eg_name == '' and Element == ''):
    #     result = HH.objects.raw(
    #         'SELECT * FROM linebotApp_HH where (number LIKE %s or number LIKE %s);', [number_like, number_like2])

    # elif(number == '' and eg_name == '' and Element == ''):
    #     result = HH.objects.raw(
    #         'SELECT * FROM linebotApp_HH where (ch_name LIKE %s or ch_name LIKE %s or ch_name LIKE %s)', [ch_like, ch_like2, ch_like3])

    # elif(number == '' and ch_name == '' and Element == ''):
    #     result = HH.objects.raw(
    #         'SELECT * FROM linebotApp_HH where (eg_name LIKE %s or eg_name LIKE %s or eg_name LIKE %s)', [eg_like, eg_like2, eg_like3])

    # elif(number == '' and ch_name == '' and eg_name == ''):
    #     result = HH.objects.raw(
    #         'SELECT * FROM linebotApp_HH where (Element LIKE %s or Element LIKE %s or Element LIKE %s)', [Element_like, Element_like2, Element_like3])

    # else:
    result = HH.objects.raw(
            'SELECT * FROM linebotApp_HH where (number LIKE %s or number LIKE %s) and (ch_name LIKE %s or ch_name LIKE %s or ch_name LIKE %s ) and (eg_name LIKE %s or eg_name LIKE %s or eg_name LIKE %s) and (Element LIKE %s or Element LIKE %s or Element LIKE %s)',
            [number_like, number_like2, ch_like, ch_like2, ch_like3, eg_like, eg_like2, eg_like3, Element_like, Element_like2, Element_like3])
    print(result.query)
    final = ''
    print("查詢數量為：" + str(len(result)))
    
    for i in result:
        final += "健保碼：" + str(i.number) + "\n" + "價格：" + \
            str(i.price) + "\n" + "成分：" + str(i.element) + "\n" + \
            "中文名稱：" + str(i.ch_name) + "\n" + \
            "英文名稱：" + str(i.eg_name) + "\n\n"
    if(len(final) >= 2000):
        final = "資料筆數過多！"
    elif(len(final) <= 0):
        final = "查無資料！"
    
    reply_arr = []

    reply_arr.append(TextSendMessage(text="查詢結果為：" + str(len(result))))
    reply_arr.append(TextSendMessage(text=final))

    print(reply_arr)
    line_bot_api.reply_message(event.reply_token, reply_arr)
    # except:
    #     line_bot_api.reply_message(
    #         event.reply_token, TextSendMessage(text='查無資料！！'))
