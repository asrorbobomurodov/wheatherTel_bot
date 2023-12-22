from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
API_KEY = os.getenv('Api_key')

import datetime
a = datetime.date.today()

print(a)