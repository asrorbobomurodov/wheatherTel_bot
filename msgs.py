from telegram import Update
from telegram.ext import CallbackContext
from settings import TOKEN



start_msg_caption = f"⛅Ob-havo ma'lumotlarni olish uchun nima qilish kerak?\n\
\n\
1) Telefoningizni boshqaruv panelidan Joylashuv (GPS) xizmatini yoqing.\n\
\n\
2) Pastda turgan \"🕹Joylashuvni yuborish\" tugmasiga bosasiz. 👇\n\
\n\
3) So'ngra OK tugmasini bosasiz va tayyor.\n\
\n\
\n\
🤔Agarda tushunmagan bo'lsangiz, rasmga e'tibor bering."

loc_msg = "<b>{country}, {region}, {city}</b>\n\
\n\
Kunlik yoki haftalik ob-havo malumotlarni ushbu tugmalar orqali oling.\n\
\n\
<i>Agarda boshqa joyni ob-havosi qiziqtirsa shunchaki menga o'sha joyni joylashuvini yuborsangiz bas.</i>"

temper = "<b>{country}, {region}, {city}</b>\n\
\n\
📆 Bugun, {today}\n\
\n\
🌤 {info_wheather}, {low}...{high}\n\
\n\
🏠 Hozir:️ {temper}°, {wind_speed} m/s\n\
\n\
⛅ Tong: {low}°\n\
🌞 Kunduzi: {high}°\n\
🌚 Kechasi:️ {low}°\n\
\n\
💧 Namlik: {namlik} %\n\
🌬 Shamol: {wind_speed} m/s\n\
🌊 Shamol yo'nalishi: {direction}\n\
🌫 Bosim: {bosim} hPa\n\
\n\
⛅ Quyosh chiqishi: {sunrise}\n\
🌥 Quyosh botishi: {sunset}"

week_info = "<b>{country} {region} viloyati</b>\n\n\
Bugun , {today}\n\
🌤 {info0}, {high0}°...{low0}°\n\
☔️  Yog'ish ehtimolligi: 0%\n\
\n\
Ertaga , {date1}\n\
☀️ {info1}, {high1}°...{low1}°\n\
☔️ Yog'ish ehtimolligi: 0%\n\
\n\
Sana:  {date2}\n\
☀️ {info2}, {high2}°...{low2}°\n\
☔️ Yog'ish ehtimolligi: 0%\n\
\n\
Sana:  {date3}\n\
☁ {info3}, {high3}°...{low3}°\n\
☔️ Yog'ish ehtimolligi: 13%\n\
\n\
Sana:  {date4}\n\
☀️ {info4}, {high4}°...{low4}°\n\
☔️ Yog'ish ehtimolligi: 0%\n\
\n\
Sana:  {date5}\n\
🌧 {info5}, {high5}°...{low5}°\n\
☔️  Yog'ish ehtimolligi: 41% \n\
\n\
Sana:  {date6} \n\
🌤 ️{info6}, {high6}°...{low6}°\n\
☔️ Yog'ish ehtimolligi: 16%"


