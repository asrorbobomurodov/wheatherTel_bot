from telegram import Update
from telegram.ext import CallbackContext
import datetime
import json
from keyboards import start_rk, wheather_keyboards
from msgs import start_msg_caption, loc_msg, temper, week_info
from wheather import wheather

def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    photo_id = 'AgACAgIAAxkBAAIBMGWBOeONNNkpP9XGBwV3kd7G-HnRAAJL1jEbPp8ISGDpHLdO_UsJAQADAgADeQADMwQ'
    user = update.effective_user
    update.message.reply_markdown_v2(
        f'*☪️Assalomu alaykum* {user.mention_markdown_v2()}\!\
\n\n*🌤Ob\-havo botiga xush kelibsiz\!*',
        reply_markup= start_rk
    )
    update.message.reply_photo(photo_id, caption=start_msg_caption)

def location(update: Update, context:  CallbackContext):
    try:
        manzil = update.message.location
        wheather_data = wheather(manzil.latitude, manzil.longitude)
        city = wheather_data['location']['city']
        country = wheather_data['location']['country']
        region = wheather_data['location']['region']
        msg1 = loc_msg.format(country=country, region=region, city=city)
        with open('location.json', 'w') as file:
            json.dump(wheather_data, file, indent=4)
        update.message.reply_html(msg1, reply_markup=wheather_keyboards)
    except KeyError:
        update.message.reply_html("<b>☹️Belgilangan manzil bo'yicha ma'lumotlar topilmadi<\b> \n Boshqa lokatsiyani belgilang! 📌")
   
def today_temp(update: Update, context: CallbackContext):
    with open('location.json', 'r') as f:
        wheather_data = json.load(f)

    city = wheather_data['location']['city']
    country = wheather_data['location']['country']
    region = wheather_data['location']['region']
    today = datetime.date.today()
    current = wheather_data['current_observation']
    temp = round((current['condition']['temperature']-32)*5/9)
    info_wheather= current['condition']['text']
    wind_speed = current['wind']['speed']
    wind_direction = current['wind']['direction']
    sunrise = current['astronomy']['sunrise']
    sunset = current['astronomy']['sunset']
    namlik = current['atmosphere']['humidity']
    bosim = current['atmosphere']['pressure']
    days : list = wheather_data['forecasts']
    low = round((days[0]['low']-32)*5/9)
    high = round((days[0]['high']-32)*5/9)
    msg2 = temper.format(country=country, region=region, city=city, 
        temper= temp, today=today, info_wheather=info_wheather, low=low,
        high=high, namlik=namlik, wind_speed=wind_speed, 
        direction=wind_direction, bosim=bosim, sunrise=sunrise, sunset=sunset)
    update.message.reply_html(msg2)

def weekly_wheather(update: Update, context: CallbackContext):
    today = datetime.date.today()
    date1 = today + datetime.timedelta(days=1)
    date2 = today + datetime.timedelta(days=2)
    date3 = today + datetime.timedelta(days=3)
    date4 = today + datetime.timedelta(days=4)
    date5 = today + datetime.timedelta(days=5)
    date6 = today + datetime.timedelta(days=6)
    with open('location.json', 'r') as f:
        wheather_data = json.load(f)
    country = wheather_data['location']['country']
    region = wheather_data['location']['region']
    days : list = wheather_data['forecasts']
    info0 = days[0]['text']
    info1 = days[1]['text']
    info2 = days[2]['text']
    info3 = days[3]['text']
    info4 = days[4]['text']
    info5 = days[5]['text']
    info6 = days[6]['text']
    low0 = round((days[0]['low']-32)*5/9)
    high0 = round((days[0]['high']-32)*5/9)
    low1 = round((days[1]['low']-32)*5/9)
    high1 = round((days[1]['high']-32)*5/9)
    low2 = round((days[2]['low']-32)*5/9)
    high2 = round((days[2]['high']-32)*5/9)
    low3 = round((days[3]['low']-32)*5/9)
    high3 = round((days[3]['high']-32)*5/9)
    low4 = round((days[4]['low']-32)*5/9)
    high4 = round((days[4]['high']-32)*5/9)
    low5 = round((days[5]['low']-32)*5/9)
    high5 = round((days[5]['high']-32)*5/9)
    low6 = round((days[6]['low']-32)*5/9)
    high6 = round((days[6]['high']-32)*5/9)
    msg3 = week_info.format(country=country, region=region,
        today=today, info0=info0, high0=high0, low0=low0,
        date1=date1, info1=info1, high1=high1, low1=low1,
        date2=date2, info2=info2, high2=high2, low2=low2,
        date3=date3, info3=info3, high3=high3, low3=low3,
        date4=date4, info4=info4, high4=high4, low4=low4,
        date5=date5, info5=info5, high5=high5, low5=low5,
        date6=date6, info6=info6, high6=high6, low6=low6,
    )

    update.message.reply_html(msg3)


    
    