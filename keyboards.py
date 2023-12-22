from telegram import ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton(text='📍 Joylashuvni yuborish', 
                      request_location=True)
start_rk = ReplyKeyboardMarkup(
    keyboard=[[btn1]],
    resize_keyboard=True
)

btn2 = KeyboardButton(text='⛅️ Bugungi ob-havo')
btn3 = KeyboardButton(text='📉 Haftalik ma\'lumot')
btn4 = KeyboardButton(text='⌚️ Soatlik ob-havo')
btn5 = KeyboardButton(text='⚙️ Botni sozlash')
btn6 = KeyboardButton(text='🇺🇿/🇷🇺 Tilni o\'zgartirish')
wheather_keyboards= ReplyKeyboardMarkup(
    keyboard=[[btn2,btn3],
                 [btn4],
              [btn5,btn6]],
    resize_keyboard = True
)